class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first > second:
                heapq.heappush(max_heap, -(first - second))
            elif second > first:
                heapq.heappush(max_heap, -(second - first))
            else:
                continue

        if not max_heap:
            return 0

        return -max_heap[0]
            
        