import hashlib
import json
import os
import re
import time
from pathlib import Path
from google import genai
from google.genai import types
import genanki

CACHE_FILE = ".card_cache.json"
OUTPUT_DECK = "neetcode.apkg"
MODEL_ID = "gemini-3.6-flash"

MODEL_ID_ANKI = 1607392319
DECK_ID_ANKI = 2059392310

CARD_CSS = """
.card {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: #24292e;
    background-color: #ffffff;
    max-width: 650px;
    margin: 0 auto;
    padding: 16px;
}
.badge {
    display: inline-block;
    padding: 2px 8px;
    font-size: 12px;
    font-weight: 600;
    border-radius: 12px;
    background-color: #f1f3f5;
    color: #495057;
    margin-right: 6px;
}
.title { font-size: 20px; font-weight: 700; margin: 8px 0 16px 0; }
ul { padding-left: 20px; margin: 8px 0; }
li { margin-bottom: 6px; }
details {
    margin-top: 16px;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    background-color: #f6f8fa;
}
summary {
    padding: 8px 12px;
    cursor: pointer;
    font-weight: 600;
    outline: none;
}
pre {
    margin: 0;
    padding: 12px;
    background-color: #1e1e1e;
    color: #d4d4d4;
    overflow-x: auto;
    border-radius: 0 0 6px 6px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 13px;
}
"""

ANKI_MODEL = genanki.Model(
    MODEL_ID_ANKI,
    "NeetCode Flashcard Model",
    fields=[
        {"name": "ProblemName"},
        {"name": "Category"},
        {"name": "ActiveRecallPrompts"},
        {"name": "KeyIntuition"},
        {"name": "Complexity"},
        {"name": "UserCode"},
    ],
    templates=[
        {
            "name": "Standard Card",
            "qfmt": """
                <div class="card">
                    <span class="badge">{{Category}}</span>
                    <div class="title">{{ProblemName}}</div>
                    <p><b>Active Recall Questions:</b></p>
                    {{ActiveRecallPrompts}}
                </div>
            """,
            "afmt": """
                {{FrontSide}}
                <hr id="answer">
                <div class="card">
                    <p><b>Key Intuition & Invariant:</b></p>
                    {{KeyIntuition}}
                    <p><b>Complexity:</b> {{Complexity}}</p>
                    <details>
                        <summary>▶ View Your Implementation</summary>
                        <pre><code>{{UserCode}}</code></pre>
                    </details>
                </div>
            """,
        }
    ],
    css=CARD_CSS,
)

def load_cache() -> dict:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}

def save_cache(cache: dict) -> None:
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)

def extract_metadata_llm(client: genai.Client, problem_name: str, code: str) -> dict:
    prompt = f"""
    Analyze this code solution for the problem "{problem_name}".
    Return a strictly valid JSON object with the following fields:
    - "active_recall_prompts": A list of 3 bullet questions testing high-level algorithmic pattern recognition, edge cases, and state invariants.
    - "key_intuition": A 2-3 sentence summary explaining the core algorithmic trick and invariant.
    - "time_complexity": Big-O notation (e.g. "O(N log N)").
    - "space_complexity": Big-O notation (e.g. "O(1)").
    - "category": High-level NeetCode topic (e.g. "Sliding Window", "Two Pointers", "Trees", "Dynamic Programming").
    """
    
    max_retries = 3
    backoff = 15

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[prompt, f"Code:\n{code}"],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.2,
                ),
            )
            return json.loads(response.text)
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                print(f"Rate limit hit for '{problem_name}'. Waiting {backoff}s before retry ({attempt + 1}/{max_retries})...")
                time.sleep(backoff)
                backoff += 15
            else:
                print(f"Non-quota API error on {problem_name}: {e}")
                break

    # Fallback if quota is exhausted or retries fail
    print(f"Using fallback summary for {problem_name}")
    return {
        "active_recall_prompts": [
            "What is the optimal data structure or pattern?",
            "What invariant or base case must be maintained?",
            "What are the target Time and Space complexities?"
        ],
        "key_intuition": "Review your implementation below for key invariants and edge cases.",
        "time_complexity": "See Implementation",
        "space_complexity": "See Implementation",
        "category": "Algorithms",
        "is_fallback": True
    }

def find_solution_files():
    valid_exts = {".py", ".java", ".cpp", ".js", ".ts", ".go"}
    ignore_dirs = {".git", ".github", ".venv", "venv", "__pycache__"}
    solutions = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for f in files:
            p = Path(root) / f
            if p.suffix in valid_exts and "test" not in f.lower():
                solutions.append(p)
    return solutions

def main():
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    cache = load_cache()
    deck = genanki.Deck(DECK_ID_ANKI, "NeetCode Practice")
    solutions = find_solution_files()

    print(f"Found {len(solutions)} solution files.")

    for path in solutions:
        problem_slug = path.parent.name if path.parent.name != "." else path.stem
        problem_name = re.sub(r"^\d+[-_]?", "", problem_slug).replace("-", " ").replace("_", " ").title()
        
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()

        file_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()

        # If not cached or if previously saved as a fallback, attempt extraction
        if file_hash not in cache or cache[file_hash].get("is_fallback"):
            print(f"Generating summary for: {problem_name}...")
            try:
                metadata = extract_metadata_llm(client, problem_name, code)
                cache[file_hash] = metadata
                save_cache(cache)
                # 6-second sleep ensures we stay comfortably under 10 RPM
                time.sleep(6.0)
            except Exception as e:
                print(f"Skipping {problem_name} due to unexpected error: {e}")
                continue
        else:
            metadata = cache[file_hash]

        prompts_html = "<ul>" + "".join(f"<li>{q}</li>" for q in metadata.get("active_recall_prompts", [])) + "</ul>"
        complexity_html = f"Time: {metadata.get('time_complexity', 'O(N)')} | Space: {metadata.get('space_complexity', 'O(1)')}"
        escaped_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        note_guid = genanki.guid_for(problem_slug)

        note = genanki.Note(
            model=ANKI_MODEL,
            fields=[
                problem_name,
                metadata.get("category", "Algorithms"),
                prompts_html,
                metadata.get("key_intuition", ""),
                complexity_html,
                escaped_code,
            ],
            guid=note_guid,
        )
        deck.add_note(note)

    save_cache(cache)
    genanki.Package(deck).write_to_file(OUTPUT_DECK)
    print(f"Deck built successfully: {OUTPUT_DECK}")

if __name__ == "__main__":
    main()