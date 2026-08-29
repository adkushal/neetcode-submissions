class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets, currset = [], []
        # Optimization sort and return early
        nums.sort()
        self.helper(0, nums, subsets, currset, target)
        return subsets



    def helper(self, i, nums, subsets, currset, remaining):
        # base case 1: No remaining, add to subsets
        if remaining == 0:
            subsets.append(currset.copy())

        # base case 2: End of range, or curr i exceeds remaining
        if i >= len(nums) or nums[i] > remaining:
            return

        # include element at i
        currset.append(nums[i])
        # IMP dont do i+1, this ensures that we repeat i multiple times
        self.helper(i, nums, subsets, currset, remaining - nums[i] )

        # Dont include element at i
        currset.pop()
        self.helper(i+1, nums, subsets, currset, remaining)
        return
        