class Solution:
    count = 0
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0]=True
        for j in range(1,len(p)+1):
            Solution.count += 1
            dp[0][j]=(dp[0][j-1] and p[j-1]=='*')
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                Solution.count += 1
                if p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                elif p[j-1] in ('?',s[i-1]):
                    dp[i][j]=dp[i-1][j-1]
        return dp[-1][-1]
s = Solution()
print(s.isMatch("bbababababbababaaababbbaaababaaababbbbabaaaaabaabbaaababbbbabbabbbaaababbabbbbbbabbabababbbbabaabaabbaaaabbaaabaaabbaabababaababbaabbbbbabbbbabbbaabbabaaaaababbbaaabbbbabaababaaaababaaaabbbaaaaaababbaaba",
"*ba**aa*aa*aa*bbba*baaba*ab*b*b*abb*b*bb*b*****a*bba**aa*b***b***aba**baa****b***a*b**ba*ba****a*aaa"))
print(Solution.count)
