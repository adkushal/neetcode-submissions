class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = nums[0]
        for num in nums[1:]:
            localMax = max(num, localMax + num)
            globalMax = max(globalMax, localMax)
        return globalMax


