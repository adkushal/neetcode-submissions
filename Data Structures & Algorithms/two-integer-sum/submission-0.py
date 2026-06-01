class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            localTarget = target - num
            if localTarget in hashMap:
                return [hashMap[localTarget], i]
            else:
                hashMap[num] = i
        return []
        