class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        if len(s) != len(t):
            return False
        for char in s:
            freq[char] +=1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    del freq[char]
            else:
                return False
        if len(freq) >0:
            return False
        return True
            
        