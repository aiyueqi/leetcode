class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        self.result = [-2] * (l+1)
        self.result[0] = -1
        return self.f(l,s)
    
    def f(self, t, s):
        if self.result[t] != -2:
            return self.result[t]
        r = t-1
        for i in range(0, t):
            if self.palindrome(s[i:t]):
                tmp = self.f(i,s)
                if tmp+1 < r:
                    r = tmp+1
        self.result[t] = r
        return r
    
    def palindrome(self, s):
        return s == s[::-1]