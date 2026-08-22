# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs_postorder(root):
            nonlocal max_diameter
            if not root:
                return 0

            left_height = dfs_postorder(root.left)
            right_height = dfs_postorder(root.right)
            # counting edges not nodes, do not add +1
            max_diameter = max(max_diameter, left_height + right_height)
            return max(left_height , right_height) + 1

        dfs_postorder(root)
        return max_diameter
        
            
        