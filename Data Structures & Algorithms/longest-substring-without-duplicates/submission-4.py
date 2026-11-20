from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = set()
        max_length = 0
        left = 0

        for i in range(len(s)):
            if s[i] in substring:
                while s[left] != s[i]:
                    substring.remove(s[left])
                    left +=1
                left+=1 # I place left on the next index of the other equal value
                # I don't need to add len[i]
            else:
                substring.add(s[i])
            max_length = max(max_length, len(substring))
        print(substring)
        return max_length