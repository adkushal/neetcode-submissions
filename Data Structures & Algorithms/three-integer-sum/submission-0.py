class Solution:
    ## Key learning, we need to check duplicates in the outer and inner loops
    ## For duplicates, check the previous value: nums[left] == nums[left - 1], 
    ## Do not check the forward value: nums[left] == nums[left + 1]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for index, value in enumerate(nums):
            # Check if value is +ve, means that solution is not possible
            if value > 0:
                break
            # check for duplicates 
            if index > 0 and value == nums[index-1]:
                continue
            
            left = index +1
            right = len(nums) -1

            while(left < right):
                three_sum = value + nums[left] + nums[right]
                if three_sum == 0:
                    solution.append([nums[index], nums[left], nums[right]])
                    # move both pointers inward
                    left += 1
                    right -= 1
                    # skip duplicates at left pointer
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1

                elif three_sum < 0:
                    left += 1
                else :
                    right -= 1

        return solution

        