class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        k_closest = []
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(heap, (distance, point))

        for i in range(k):
            distance, point = heapq.heappop(heap)
            k_closest.append(point)
        return k_closest
        