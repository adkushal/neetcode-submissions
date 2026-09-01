class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Slow pointer where we write
        write = 1
        # Read is the fast pointer scanning the array
        for read in range(1, len(nums)):
            if nums[write-1] != nums[read]:
                nums[write] = nums[read]
                # move write forward
                write += 1
            
        return write







        