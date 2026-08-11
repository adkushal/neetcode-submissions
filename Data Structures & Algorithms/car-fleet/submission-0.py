class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Use the concept of monotonic stack
        # Start with creating position:time tuples

        position_time = []
        stack = []
        for pos, spd in zip(position, speed):
            time = (target - pos) / spd
            position_time.append((pos, time))

        position_time.sort()

        for pos, time in position_time:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)

            
