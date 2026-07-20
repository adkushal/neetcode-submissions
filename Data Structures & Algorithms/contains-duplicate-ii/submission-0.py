class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = set()
        left = 0
        ## if k = 1, it can contain 2 elements
        ## if k = 2, it can contain 3 elements
        ## we do right - left so that it can contant k+1 elements
        ## This corresponds to abs(k) away
        for right in range(len(nums)):
            if right - left > k:
                duplicates.remove(nums[left])
                left += 1
            if nums[right] in duplicates:
                return True
            duplicates.add(nums[right])
        return False
        