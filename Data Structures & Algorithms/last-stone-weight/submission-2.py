class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            # First biggest
            first = -heapq.heappop(max_heap)
            # second biggest
            second = -heapq.heappop(max_heap)

            # They could be equal
            if first > second:
                heapq.heappush(max_heap, -(first - second))
            else:
                continue

        if not max_heap:
            return 0

        return -max_heap[0]
            
        