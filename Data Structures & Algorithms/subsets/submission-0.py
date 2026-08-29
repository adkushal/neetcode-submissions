class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # keeps track of the return val, ie all the subsets
        subsets = []

        # keep track and build the individual subsets
        currset = []
            
        self.helper(0, nums, subsets, currset)
        return subsets

    def helper(self, i, nums, subsets, currset):
        # base case, check if i is greater than nums size
        if i >= len(nums):
            subsets.append(currset.copy())
            return


        # include element at i
        currset.append(nums[i])
        self.helper(i+1, nums, subsets, currset)

        # Dont include element at i
        currset.pop()
        self.helper(i+1, nums, subsets, currset)
        return


        