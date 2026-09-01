class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Slow pointer where we write
        write = 0
        # Read is the fast pointer scanning the array
        for read in range(1, len(nums)):
            if nums[write] != nums[read]:
                # move write forward
                write += 1
                nums[write] = nums[read]
            
        return write + 1







        