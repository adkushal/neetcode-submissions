import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    ret_list = []
    for num in nums:
        heapq.heappush(heap, (-num, num))
    while(heap):
        pair = heapq.heappop(heap)
        ret_list.append(pair[1])
    return ret_list



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
