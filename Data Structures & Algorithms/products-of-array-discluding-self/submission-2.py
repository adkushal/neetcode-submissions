class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## We create two prefix lists 
        # Input: [a, b, c, d]
        # 1. [1, a, a*b, a*b*c] -> Everything before i
        # 2. [b*c*d, c*d, d, 1] -> Everything after i

        left_prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            left_prefix[i] = left_prefix[i-1] * nums[i-1]

        right_prefix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right_prefix[i] = right_prefix[i+1] * nums[i+1]

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = left_prefix[i] * right_prefix[i] 
        return result


