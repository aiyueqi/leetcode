from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            if i == len(p):
                return False

            result = False
            if p[j] == "*":
                for k in range(i, len(s)+1):
                    result = result or dp(k, j+1)
            else:
                result = (s[i] in {p[j], '?'}) and dp(i+1, j+1)
            mem[(i,j)] = result
            return result
        r =  dp(0, 0)
        print(mem)
        return r
        
s = Solution()
print(s.isMatch("adced", "*a*b"))
