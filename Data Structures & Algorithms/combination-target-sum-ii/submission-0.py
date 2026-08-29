class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sublists, currlist = [], []
        candidates.sort()
        self.helper(0, candidates, sublists, currlist, target)
        return sublists

    def helper(self, i, candidates, sublists, currlist, remaining):
        # Base case 1
        if remaining == 0:
            sublists.append(currlist.copy())
            return
        
        # base case 2
        if i >= len(candidates) or candidates[i] > remaining:
            return

        # include i
        currlist.append(candidates[i])
        self.helper(i+1, candidates, sublists, currlist, remaining - candidates[i])

        # exclude i
        currlist.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i +=1
        self.helper(i+1, candidates, sublists, currlist, remaining)
        return

        