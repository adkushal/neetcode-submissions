# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited_count = 0
        ans = None

        def inorderDFS(root):
            nonlocal visited_count
            nonlocal ans

            if not root or ans:
                return

            inorderDFS(root.left)

            # Visit the current node
            visited_count += 1
            if visited_count == k:
                ans = root.val

            inorderDFS(root.right)

        inorderDFS(root)
        return ans
        