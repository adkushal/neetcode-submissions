class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets, currset = [], []
        self.helper(0, nums, subsets, currset, target)
        return subsets



    def helper(self, i, nums, subsets, currset, target):
        # base case, check if i is greater than nums size
        total = sum(currset)
        if i >= len(nums):
            if total == target:
                subsets.append(currset.copy())
            return


        if total > target:
                return

        # include element at i
        currset.append(nums[i])
        self.helper(i, nums, subsets, currset, target)

        # Dont include element at i
        currset.pop()
        self.helper(i+1, nums, subsets, currset, target)
        return
        