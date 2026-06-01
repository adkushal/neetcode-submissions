class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        
        for char in t:
            if char in hashMap:
                hashMap[char] -= 1
                if hashMap[char] == 0:
                    del hashMap[char]
            else:
                return False

        return not hashMap

        