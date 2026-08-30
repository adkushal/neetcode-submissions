class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subsets, currset = [], []
        self.helper(1, n, k, subsets, currset)
        return subsets


    def helper(self, i, n, k, subsets, currset):
        # Base case, we reached k values in the currset
        if len(currset) == k:
            subsets.append(currset.copy())

        # Base case, i did not add anything to curr set and reached end
        if i > n:
            return

        # For combinations (ie not subsets), 
        # explore only forward elements (j >= i) to avoid permutations like [2, 1] after [1, 2].
        for j in range(i, n+1):
            # include j
            currset.append(j)
            self.helper(j+1, n, k, subsets, currset)

            # backtrack and do not include j
            currset.pop()


        