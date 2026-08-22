# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs_postorder(root, depth):
            if not root:
                return 0

            left_depth = dfs_postorder(root.left, 0)
            right_depth = dfs_postorder(root.right, 0)

            return max(left_depth, right_depth) + 1

        return dfs_postorder(root, 0)
        