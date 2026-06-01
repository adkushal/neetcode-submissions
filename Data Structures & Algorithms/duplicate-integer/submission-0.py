class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for item in nums:
            if item not in hashMap:
                hashMap[item] = 1
            else:
                return True
        return False
        