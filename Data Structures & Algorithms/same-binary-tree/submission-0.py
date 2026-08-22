# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        is_valid = True

        def dfs_postorder(root):
            nonlocal stack
            if not root:
                stack.append(-101)
                return

            dfs_postorder(root.left)
            dfs_postorder(root.right)
            stack.append(root.val)

        def dfs_reverse_postorder(root):
            nonlocal stack
            nonlocal is_valid
            if not root:
                if stack and stack[-1] == -101:
                    stack.pop()
                else:
                    is_valid = False
                return

            if stack and stack[-1] == root.val:
                stack.pop()
            else:
                is_valid = False
                return

            dfs_reverse_postorder(root.right)
            dfs_reverse_postorder(root.left)

        dfs_postorder(p)
        dfs_reverse_postorder(q)

        return is_valid and len(stack) == 0
            
        