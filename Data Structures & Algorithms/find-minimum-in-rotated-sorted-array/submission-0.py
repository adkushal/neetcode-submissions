class Solution:
    """
    We need to find the pivot element that's the min element
    1. Perform regular binary sort
    2. It will alway split into two groups, one sorted, and one with the pivot element thats unsorted
    3. Discard the sorted group and perform binary sort on the unsorted group
    4. When low = high, we have found the pivot element
    """
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) -1

        while low < high:
            mid = (low + high) // 2
            #Check if right half is unsorted
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                

        return nums[low]


        