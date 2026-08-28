class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TreeNode()
            curr = curr.children[ch]
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(node, word):
            # Check the end cases
            # No children left
            if not node:
                return False

            # No word characters left, but node not a word
            if len(word) == 0 and not node.isWord:
                return False

            # Success case, no chars left, and node is a word
            if len(word) == 0 and node.isWord:
                return True

            # chars left, search in children
            # First char of word
            ch = word[0]
            # is a "."
            if ch == ".":
                result = False
                for child in node.children.values():
                    result = result or dfs(child, word[1:])
                return result

            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], word[1:])

        return dfs(self.root, word)
            



            
        
