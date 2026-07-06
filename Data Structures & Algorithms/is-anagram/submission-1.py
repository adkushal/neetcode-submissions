class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for char in s:
            if char in check:
                check[char] += 1
            else:
                check[char] = 1
        itr = 0
        for char in t:
            itr +=1
            if char in check:
                check[char] -= 1
                if check[char] == 0:
                    del check[char]
                    
            else:
                return False
        print(len(check))
        if itr < len(t) or len(check) > 0:
            return False
        else:
            return True
        