class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max_sequence = min(len(nums), 1)
        current_sequence = min(len(nums), 1)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] == nums[i+1] - 1:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 1
        return max(max_sequence, current_sequence)