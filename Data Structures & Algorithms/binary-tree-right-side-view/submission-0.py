# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret_list = []
        if not root:
            return ret_list

        queue = deque()
        queue.append(root)
        
        while(len(queue) > 0):
            add_val = None
            loop_len = len(queue)
            for i in range(loop_len):
                node = queue.popleft()
                add_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret_list.append(add_val)
        return ret_list
        
        