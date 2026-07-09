class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) +1)]
        res = []

        for key, value in freq.items():
            buckets[value].append(key)

        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res



        