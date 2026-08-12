class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        max_area = 0
        stack = []

        for i, height in enumerate(heights):

            ## Pop while stack is not empty and top of stack is > height
            # This keeps the stack monotonic (increasing order)
            while stack and heights[stack[-1]] > height:
                # pop the highest element seen at top of stack
                current_highest_index = stack.pop()

                # If stack is empty, width is i, 
                # If not empty, width is i - next_highest_index -1, 
                # length is current_highest_hight for both

                if not stack:
                    width = i

                else:
                    next_highest_index = stack[-1]
                    width = i - next_highest_index -1
                
                length = heights[current_highest_index]
                max_area = max(max_area, length * width)

            
            # Add current to stack
            stack.append(i)

        return max_area

        