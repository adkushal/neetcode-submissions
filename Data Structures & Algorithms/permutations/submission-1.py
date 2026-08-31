class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
        

    def helper(self, i, nums):
        # base case, return the empty list of perms that will be 
        # operated on
        if i == len(nums):
            return [[]]

        # recuse to reach above base base
        perms = self.helper(i+1, nums)

        """
        Everything above in this recursive solution is just to return [[]]
        Prefer to do this iteratively
        Diff is recursive operates on nums from back to start
        """
        res_perms = []
        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                res_perms.append(p_copy)
        return res_perms
        



