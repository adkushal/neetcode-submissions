class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort(reverse = True)
        # single element means we return 1 sequence
        ret_count = 1
        local_count = 1
        prev = nums[0]

        for num in nums:
            # if repreat
            if num == prev:
                continue
            elif num +1 == prev:
                local_count += 1
                ret_count = max(ret_count, local_count)
            else:
                # reinitialize to base case ie 1
                local_count = 1
            prev = num

        return ret_count

        