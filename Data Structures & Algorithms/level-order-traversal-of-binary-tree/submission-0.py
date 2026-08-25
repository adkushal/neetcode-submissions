# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret_list = []
        queue = deque()
        if not root:
            return ret_list
        
        queue.append(root)
        while len(queue) > 0 :
            local_list = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                local_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret_list.append(local_list)

        return ret_list
            




        


        