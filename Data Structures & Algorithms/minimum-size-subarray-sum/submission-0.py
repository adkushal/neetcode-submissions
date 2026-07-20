class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, count, running_sum = 0, 0, 0
        min_size = float("inf")
        for right in range(len(nums)):
            running_sum += nums[right]
            count += 1
            while(running_sum >= target):
                min_size = min(min_size, count)
                running_sum -= nums[left]
                left += 1
                count -= 1
        if min_size == float("inf"):
            return 0
        return min_size