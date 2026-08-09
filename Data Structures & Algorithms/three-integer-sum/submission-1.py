class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## The Idea is to have:
        # 1. Sort the input O(n log n)
        # 2. Outer loop left to right, skipping duplicates O(n)
        # 3. Inner loop computing 2 Sum (2 pointer version), O(n)
        # Complexity = O(nlogn) + O(n)^2 = O(n)^2
        prev = None
        result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            # First check if i was repeated last iteration
            check = nums[i]
            if check == prev:
                continue

            two_sum = self.twoSum(nums[i+1:], -check)
            if len(two_sum) > 0:
                # Add check into each retuned 2 sum list
                for sub_list in two_sum:
                    sub_list.append(check)
                result.extend(two_sum)

            prev = nums[i]

        return result

    # There be more than one pair that satisfies the sum
    # Also skip duplicate 
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        left = 0
        right = len(nums) -1
        while(left < right):
            localTarget = nums[left] + nums[right]
            if localTarget == target:
                res.append([nums[left], nums[right]])
                left +=1
                right -=1
                # Skip identical elements to avoid duplicate triplets
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif localTarget < target:
                left +=1
            else:
                right -=1
        return res