class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            if curSum < 0:
                curSum = num
            else:
                curSum += num
            
            maxSum = max(curSum, maxSum)
        return maxSum

        