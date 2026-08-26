# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        root_val = root.val
        good_node_count = 0

        def dfs_postorder(root, max_so_far):
            nonlocal good_node_count
            if not root:
                return

            if root.val >= max_so_far:
                good_node_count += 1

            left_good_nodes = dfs_postorder(root.left, max(root.val, max_so_far))
            right_good_nodes = dfs_postorder(root.right, max(root.val, max_so_far))

        dfs_postorder(root, float("-inf"))
        return good_node_count

             