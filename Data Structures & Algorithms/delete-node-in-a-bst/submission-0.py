# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMinNode(self, root:  Optional[TreeNode]) -> Optional[TreeNode]:
        while root and root.left:
            root = root.left

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Base case to stop when we go beyond leaf nodes
        # If tree is non empty and guaranteed to contain the key, this will 
        # NEVER get triggered

        if not root:
            return None

        # Traverse until we reach the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # key = root.val
        else:
            # Case 0 child
            if not root.left and not root.right:
                # The parent root.left or root.right gets assigned None
                return None

            # Case 1 child
            if not root.left:
                # The parent gets assigned the right child
                return root.right

            if not root.right:
                # The parent gets assigned the left child
                return root.left

            # Case 2 children
            # REPLACE the node value with the smallest among the nodes larger than node value
            min_node = self.findMinNode(root.right)
            root.val = min_node.val

            # delete the min_node
            root.right = self.deleteNode(root.right, min_node.val)
        
        #ensures every non-deleted node properly returns its own reference back up the tree
        return root
        