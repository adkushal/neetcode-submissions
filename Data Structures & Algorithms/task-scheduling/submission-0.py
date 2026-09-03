class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-ctr for ctr in count.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:
            # Important to increment time first
            time += 1

            # Fetch available element from queue and add back to heap
            if queue and queue[0][1] <= time:
                element, timeout = queue.popleft()
                heapq.heappush(max_heap, element)

            if max_heap:
                element = heapq.heappop(max_heap)
                element += 1
                if element < 0:
                    # Add the current element to the queue with timeout + 1
                    # +1 is needed so that we pick it up after timeout
                    queue.append((element, time + n + 1))
        
        return time
        