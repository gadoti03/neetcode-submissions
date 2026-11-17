class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix = [nums[0]]*n
        suffix = [nums[-1]]*n
        output = []

        for i in range(1, n):
            prefix[i] = nums[i]*prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i]*suffix[i+1]
        for i in range(n):
            pre = prefix[i-1] if i-1>=0 else 1
            suc = suffix[i+1] if i+1<n else 1 
            output.append(pre*suc)
        return output

        # Complexity
        # O(n)
        #
        # Improvements
        # I can achieve O(1) in auxiliar memory
        
        # Strategy
        # Prefix/Suffix