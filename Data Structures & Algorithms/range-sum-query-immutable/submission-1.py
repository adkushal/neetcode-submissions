class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix[i] = self.prefix[i-1] + nums[i-1]


        

    def sumRange(self, left: int, right: int) -> int:
        # prefix[index] contains all numbers up until the index (excludes the index)
        # Since we want to include right, we do prefix[right + 1]
        return self.prefix[right + 1] - self.prefix[left] 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)