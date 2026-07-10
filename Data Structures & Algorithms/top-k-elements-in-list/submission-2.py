class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1 

        for value, count in freq.items():
            heapq.heappush(minheap, (count, value))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        retlist = []
        for count, value in minheap:
            retlist.append(value)
        return retlist