class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sums = {0:1}
        count = 0
        accumulated = 0

        for val in nums:
            accumulated += val
            target = accumulated - k
            if target in seen_sums:
                count += seen_sums[target]
            seen_sums[accumulated] = seen_sums.get(accumulated,0) +1
        return count
