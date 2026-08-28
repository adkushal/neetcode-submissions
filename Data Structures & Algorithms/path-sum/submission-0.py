# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs_greedy(root, current_sum):
            if not root:
                return False

            total_sum = current_sum + root.val
            if not root.left and not root.right and total_sum == targetSum:
                return True

            # greedily go left
            if dfs_greedy(root.left, total_sum):
                return True
            
            # greedily go right
            if dfs_greedy(root.right, total_sum):
                return True

            # backtrack
            return False
        
        return dfs_greedy(root, 0)