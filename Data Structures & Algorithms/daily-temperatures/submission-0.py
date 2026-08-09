class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            if not stack:
                stack.append(i)

            while stack and temperatures[stack[-1]] < value:
                pop_index = stack.pop()
                difference_days = i - pop_index
                results[pop_index] = difference_days

            stack.append(i)

        return results

        