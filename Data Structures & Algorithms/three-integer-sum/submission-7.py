from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        s = set()
        d = defaultdict(int)

        # populate defaultdict
        for num in nums:
            d[num]+=1

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                val = nums[i]+nums[j]

                d[nums[i]]-=1
                d[nums[j]]-=1
                if d[-val]:
                    l = [nums[i], nums[j], -val]
                    l.sort()
                    t = (l[0], l[1], l[2])
                    s.add(t)
                d[nums[i]]+=1
                d[nums[j]]+=1
                
        return list(s)