class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        subsets, currset = [], []
        
        # Edge case, empty string
        if len(digits) == 0:
            return subsets
        self.helper(0, subsets, currset, digits, phone_dict)
        return subsets

    def helper(self, i, subsets, currset, digits, phone_dict):
        # base case, we reach the number of digit combinations:
        if len(currset) == len(digits):
            subsets.append("".join(currset.copy()))
            return

        # base case, we do not choose any combination ?
        if i >= len(digits):
            return

        for char in phone_dict[digits[i]]:
            # include the char
            currset.append(char)
            self.helper(i+1, subsets, currset, digits, phone_dict)

            # remove and backtrack
            currset.pop()
        return

    
        