class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set(nums)
        global_max = 1

        for num in seen:
            # check if the num in the start of a sequence
            check = num + 1
            local_max = 1
            while check in seen and num-1 not in seen:
                local_max += 1
                global_max = max(global_max, local_max)
                check += 1

        return global_max

        