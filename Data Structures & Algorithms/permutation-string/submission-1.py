from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = set()
        d = defaultdict(int)
        n = len(s1)
        for c in s1:
            s.add(c)
            d[c]+=1

        left = 0
        for i in range(len(s2)):
            if d[s2[i]]:
                d[s2[i]]-=1
                n-=1
                if n == 0:
                    return True
            elif s2[i] in s:
                while s2[left] != s2[i]:
                    d[s2[left]]+=1
                    left+=1
                    n+=1
                left+=1
            else:
                # restore dictionary
                while left < i:
                    d[s2[left]]+=1
                    n+=1
                    left+=1
                left+=1
        return False