class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets_map = {')':'(', '}':'{', ']':'['}
        #closing_brackets = set(')', '}', ']')

        for char in s:
            if char not in brackets_map.keys():
                stack.append(char)
            else:
                top = stack[-1] if stack else None
                if top != brackets_map[char]:
                    return False
                stack.pop()
        return not stack 



        