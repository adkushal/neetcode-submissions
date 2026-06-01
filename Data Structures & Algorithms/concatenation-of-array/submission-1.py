class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums + nums
        size = len(nums)
        ans = [0] * size * 2
        for i, num in enumerate(nums):
            ans[i] = ans[i + size] = num

        return ans
