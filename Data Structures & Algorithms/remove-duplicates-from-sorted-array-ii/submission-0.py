class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 0 and 1 dont need any processing
        if len(nums) < 2:
            return len(nums)
        
        write = 2
        for read in range(2, len(nums)):
            # normally we check write -1
            # since we can have 1 duplicate, only check write -2
            if nums[write -2] != nums[read]:
                nums[write] = nums[read]
                write +=1
        return write