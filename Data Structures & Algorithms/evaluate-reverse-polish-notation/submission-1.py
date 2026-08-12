import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Map strings to functions
        operands = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv

        }
        stack = []
        for token in tokens:
            if token not in operands.keys():
                stack.append(int(token))

            else:
                second = stack.pop()
                first = stack.pop()
                target = operands[token](first,second)
                stack.append(int(target))

        return stack[-1]


        