class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, subsets = [], []
        self.helper(nums, 0, currset, subsets)
        return subsets


    def helper(self, nums, i, currset, subsets):
        if i >= len(nums):
            subsets.append(currset.copy())
            return
        
        # include i
        currset.append(nums[i])
        self.helper(nums, i+1, currset, subsets)

        # dont include i, or any repeat occourances of i
        currset.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(nums, i+1, currset, subsets)
        