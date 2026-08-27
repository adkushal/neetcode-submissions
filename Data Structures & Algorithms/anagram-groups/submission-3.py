class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        retList = []
        for value in strs:
            key = sorted(value)
            anagrams[tuple(key)].append(value)

        for value in anagrams.values():
            retList.append(value)

        return retList

        