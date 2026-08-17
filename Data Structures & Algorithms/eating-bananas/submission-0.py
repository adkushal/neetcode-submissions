class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Sort the input array
        piles.sort()

        low = 1
        high = piles[-1]

        #  Adjust binary search to find the leftmost (minimum) valid k
        while low < high:
            mid = (low + high) // 2
            check_hours_res = self.checkHours(piles, h, mid)

            if check_hours_res >= 0:
                high = mid

            else:
                low = mid+1

        return low


    # Returns -1 if k is too small and we do not eat all bananas
    # +1 if k is too large and we have remaining hours h left
    # 0 if we do not have any hours left after eating all the bananas
    def checkHours(self, piles: List[int], h: int, k: int) -> int:
        hours_eating = 0
        for pile in piles:
            hours_eating += math.ceil(pile / k)

        if hours_eating == h:
            return 0

        ## k is too small, we ran out of time
        elif hours_eating > h:
            return -1

        ## k is too large, we have time ledt
        else:
            return 1

        