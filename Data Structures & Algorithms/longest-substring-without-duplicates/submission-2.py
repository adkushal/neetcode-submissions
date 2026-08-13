class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left, max_substring = 0, 0

        if len(s) < 2:
            return len(s)

        unique.add(s[0])
        for right in range(1, len(s)):

            # Check if right char is in the set
            while s[right] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[right])
            max_substring = max(max_substring, right - left + 1)
        return max_substring

        