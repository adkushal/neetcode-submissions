class Solution:
    """
    We perform normal binary search, we get either 
    1. left half sorted, and right half has pivot point
    2. right half sorted, and left half has pivot point

    Irrespective check within the sorted portion has the target is within its range,
    - If yes, perform binary search in the portion,
    - If no, perform binary search in the remaining portion

    """
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid
            ## check if left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid +1

            ## else right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid +1
                else:
                    high = mid -1

        return -1
        