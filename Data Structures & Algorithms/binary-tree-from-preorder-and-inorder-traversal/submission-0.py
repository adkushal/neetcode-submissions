# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Build a map value -> index using the inorder list
        inorder_map = { val:i  for i, val in enumerate(inorder)}
        # node_index keep track of the preorder list
        node_index = 0

        def helper(left_segment, right_segment):
            nonlocal node_index

            # Base case for leaf nodes
            # works for building left sub tree and right subtree because we will get
            # left sub tree -> 0, -1 and right subtree -> 1, 0
            if left_segment > right_segment:
                return None

            # Since we keep updating node_index, we process the elements in preorder
            # root first, then left, then right
            root_val = preorder[node_index]
            node_index += 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            root.left = helper(left_segment, mid-1)
            root.right = helper(mid+1, right_segment)
            return root

        return helper(0, len(inorder)-1)

        