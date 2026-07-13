class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # Answer[48,24,12,8]

        # Forward [1, 1, 2, 8]
        # Backward [48, 24, 6, 1]

        forward = [1] * len(nums)
        backward = [1] * len(nums)

        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i+1] * nums[i+1]

        result = [0] * len(nums)
        for i in range(0, len(nums)):
            result[i] = forward[i] * backward[i]

        return result



        