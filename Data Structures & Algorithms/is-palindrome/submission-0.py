class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_s = []
        for c in s.lower():
            if c.isalnum():
                list_s.append(c)
        left = 0
        right = len(list_s)-1
        while left < right:
            if list_s[left] != list_s[right]:
                return False
            left+=1
            right-=1
        return True