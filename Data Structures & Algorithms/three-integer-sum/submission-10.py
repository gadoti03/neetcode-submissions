from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dim = len(nums)
        output = []

        print(nums, dim)

        for i in range(dim-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left = i+1
            right = dim-1

            while left < right:
                val = nums[left] + nums[right]
                if val < target:
                    left+=1
                elif val > target:
                    right -=1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    left+=1
                    right-=1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
        
        return output

        # Complexity
        # O(n^2)
        #
        # harness the sorting (fix the first digit, interato on the other 2)