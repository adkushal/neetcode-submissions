class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        ## There are 4 cases to handle
        ## 1. solution is a subarray in the normal bounds of the list
        ## 2. Solution wraps around the list
        ## 3. All are -ve

        global_min = nums[0]
        local_min = nums[0]
        global_max = nums[0]
        local_max = nums[0]
        sum_array = nums[0]
        for i in range(1, len(nums)):
            # Find the min sub array
            local_min = min(nums[i], local_min + nums[i])
            global_min = min(global_min, local_min)

            # Find the max sub array
            local_max = max(nums[i], local_max + nums[i])
            global_max = max(global_max, local_max)

            # Find the sum as well while we are in the loop
            sum_array += nums[i]
        wrap_solution = sum_array - global_min

        # Temp solution works if we have a mix of -ve and +ve elements

        ## All elements are -ve, return the largest element
        # global_max would be -ve if all values are infact -ve
        if global_max < 0:
            return  global_max

        # Base case, mix of -ve and +ve elements
        return max(global_max, wrap_solution)