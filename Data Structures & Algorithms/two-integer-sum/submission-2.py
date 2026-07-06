class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            if target - num in check:
                return [check[target - num], i]
            else:
                check[num] = i
        return []
        