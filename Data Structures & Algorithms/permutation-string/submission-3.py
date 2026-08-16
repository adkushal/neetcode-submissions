class Solution:
    # This exactly follows the fixed window size algo
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = defaultdict(int)
        seen_map = defaultdict(int)
        window = len(s1)
        for char in s1:
            freq_map[char] += 1
        left = 0
        for right in range(len(s2)):
            # Check if we exceeded the window:
            if right - left + 1 > window:
                seen_map[s2[left]] -= 1
                if seen_map[s2[left]] == 0:
                    del seen_map[s2[left]]
                left += 1

            # Check window condition
            seen_map[s2[right]] += 1
            if freq_map == seen_map:
                return True

        return False
