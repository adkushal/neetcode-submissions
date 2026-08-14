class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        # the char to frequency map 
        freq = defaultdict(int)

        # he largest substring after replacements
        max_replacement = 0

        # the largest frequency character seen so far
        # This gets fixed and keeps the window wide to avoid checking in smaller windows
        max_freq_char = 0
        left = 0
        
        for right in range(0, len(s)):
            freq[s[right]] += 1
            max_freq_char = max(max_freq_char, freq[s[right]])

            # Check if window is invalid
            while right - left + 1 > max_freq_char + k:
                freq[s[left]] -= 1
                left += 1

            max_replacement = max(max_replacement, right - left + 1)

        return max_replacement

        