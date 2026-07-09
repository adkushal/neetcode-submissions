class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3
        for num in nums:
            freq[num] += 1
        
        i = 0
        for index, count in enumerate(freq):
            for j in range(count):
                nums[i] = index
                i+=1
        return nums
        