class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        size = []
        strings = []
        for string in strs:
            size.append(str(len(string)))
            size.append(",")
            strings.append(string)
        size[-1] = "#"
        retval =  "".join(size + strings)
        return retval

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        delimiter = s.find("#")
        sizestr = s[ : delimiter]
        strings = s[delimiter+1: ]
        size = [int(s) for s in sizestr.split(",")]
        
        retval = []
        start  = 0
        end = 0
        for i in size:
            end = i + end
            listval = strings[start: end]
            retval.append(listval)
            start += i

        return retval



