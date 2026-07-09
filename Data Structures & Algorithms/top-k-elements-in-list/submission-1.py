class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) +1)]
        res = []

        for key, value in freq.items():
            buckets[value].append(key)

        ## Now we have an array where index is freq and values is
        # a list of items with that frequency
        for frequency in range(len(buckets)-1, 0, -1):
            for item in buckets[frequency]:
                res.append(item)
                if len(res) == k:
                    return res



        