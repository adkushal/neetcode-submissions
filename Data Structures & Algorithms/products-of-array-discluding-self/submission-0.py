class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i-1]

        for j in range(len(nums) -2, -1, -1):
            backward[j] = backward[j+1] * nums[j+1]

        print(forward)
        print(backward)

        res = [0] * len(nums)
        for k in range(len(nums)):
            res[k] = forward[k] * backward[k]
        return res



        