class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        duplicate = set()
        max_length = float("-inf")
        left = 0
        for right in range(len(s)):
            while s[right] in duplicate:
                duplicate.remove(s[left])
                left += 1
            duplicate.add(s[right])
            max_length = max(max_length, len(duplicate))
        return max_length


        