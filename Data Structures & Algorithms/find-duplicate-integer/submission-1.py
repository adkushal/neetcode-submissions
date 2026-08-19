class Solution:
    """
    pigeon hole principle
    every value is guranteed to also be an index in the array
    nums = [1,2,3,2,2]
    index = [0,1,2,3,4]

    start at index 0
    nums[0] -> 1
    nums[1] -> 2
    nums[2] -> 3
    nums[3] -> 2
    nums[2] -> 3

    We found a loop in the list. Use a slow and fast pointer
    to implement tortoise and hare algo to find the loop

    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # finds a collision in the loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find start of the loop
        first = 0
        while first != slow:
            slow = nums[slow]
            first = nums[first]

        return slow

        