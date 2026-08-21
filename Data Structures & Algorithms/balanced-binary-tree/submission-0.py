# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solve using DFS and in a bottom up manner
each function checks two things:
 - Is the left subtree balanced
 - Is the right sub tree balanced
 - Is the current node balanced by checking the left and right heights
 - Finally return a Tuple (isBalanced, height)
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_bottom_up_height(root):
            if not root:
                # Return 0 height, is True balanced as base case
                return (True, 0)

            # Iterate to left subtree
            # Unpack tuple
            is_left_balanced, left_height = dfs_bottom_up_height(root.left)

            # Iterate to right subtree
            is_right_balanced, right_height = dfs_bottom_up_height(root.right)

            # Check if both subtrees are balanced and 
            # current node is balanced

            is_root_balanced = is_left_balanced and is_right_balanced and (abs(left_height - right_height) <= 1)

            return (is_root_balanced, max(left_height, right_height) + 1)

        is_balanced, max_height = dfs_bottom_up_height(root)
        return is_balanced



        