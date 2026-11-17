class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        for c in s:
            if c in d_s:
                d_s[c] = d_s[c] + 1
            else:
                d_s[c] = 1
        for c in t:
            if c in d_s:
                if d_s[c] > 1:
                    d_s[c] = d_s[c]-1
                else:
                    del d_s[c]
            else:
                return False
        if not d_s:
            return True
        return False
