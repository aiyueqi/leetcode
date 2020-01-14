from typing import *

class Solution:
    count = 0
    def isMatch(self, s: str, p: str) -> bool:
        mem = [[-1]*(len(p)+1) for i in range(0, len(s)+1)]
        def dp(i, j):
            if mem[i][j] != -1:
                return mem[i][j]
            Solution.count += 1
            if j == len(p):
                return i == len(s)

            result = False
            if p[j] == "*":
                for k in range(i, len(s)+1):
                    result = result or dp(k, j+1)
            else:
                if i == len(s):
                    return False
                result = (p[j] in {s[i], '?'}) and dp(i+1, j+1)
            mem[i][j] = result
            return result
        return dp(0,0)
        
s = Solution()
print(s.isMatch("bbababababbababaaababbbaaababaaababbbbabaaaaabaabbaaababbbbabbabbbaaababbabbbbbbabbabababbbbabaabaabbaaaabbaaabaaabbaabababaababbaabbbbbabbbbabbbaabbabaaaaababbbaaabbbbabaababaaaababaaaabbbaaaaaababbaaba",
"*ba**aa*aa*aa*bbba*baaba*ab*b*b*abb*b*bb*b*****a*bba**aa*b***b***aba**baa****b***a*b**ba*ba****a*aaa"))
print(Solution.count)
