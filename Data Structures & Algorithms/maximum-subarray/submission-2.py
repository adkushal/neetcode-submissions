class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Concept here is that if we previous saw a large -ve number which made the 
        # sum -ve, then we are better off starting fresh from the next element
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            if curSum < 0:
                curSum = num
            else:
                curSum += num
            
            maxSum = max(curSum, maxSum)
        return maxSum

        