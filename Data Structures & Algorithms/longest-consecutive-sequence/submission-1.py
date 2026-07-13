class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        global_max = 1
        local_max = 1
        count = set()

        for num in nums:
            count.add(num)

        for values in count:
            # first check if we are at the begining of
            # the sequence
            if values - 1 not in count:
                # Check for the next element in the sequence
                while values + 1 in count:
                    local_max += 1
                    global_max = max(global_max, local_max)
                    values = values +1
            local_max = 1

        return global_max
            

            




        