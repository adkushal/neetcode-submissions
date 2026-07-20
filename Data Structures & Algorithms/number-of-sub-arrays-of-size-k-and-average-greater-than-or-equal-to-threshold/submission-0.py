class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        sum_of = 0
        solution = 0
        for right in range(len(arr)):
            sum_of += arr[right]
            if right - left +1 == k:
                avg = sum_of / k
                if avg >= threshold:
                   solution += 1 
                sum_of -= arr[left]
                left += 1
        return solution

            

        