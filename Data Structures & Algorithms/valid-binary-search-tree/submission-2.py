# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def helper(root, min, max):
            if not root:
                return True

            if root.val <= min or root.val >= max:
                return False

            return helper(root.left, min, root.val) and helper(root.right, root.val, max)

        return helper(root.left, float("-inf"), root.val) and helper(root.right, root.val, float("inf"))
        