class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] -= 1
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))

        for i in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)

        return res


        