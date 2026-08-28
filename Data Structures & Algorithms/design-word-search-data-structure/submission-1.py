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
            if not node:
                return False

            if len(word) == 0 and node.isWord:
                return True

            if len(word) == 0 and not node.isWord:
                return False

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
            



            
        
