class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        output = 0
        while s:
            n = s.pop()
            i_min = 0
            while (n-1-i_min) in s:
                s.remove(n-1-i_min)
                i_min+=1
            i_max = 0
            while (n+1+i_max) in s:
                s.remove(n+1+i_max)
                i_max+=1
            output = max(output, i_min+i_max+1)
        return output