class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict() # 备忘录
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
    
        return dp(0, 0)