class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        result = [float('inf')] * (l+1)
        result[0] = -1
        ispalindrome = [[True for i in range(l)] for j in range(l)]

        for t in range(1, l+1):
            for i in range(0, t):
                #if palindrome(s[i:t]):
                if self.palindrome(s, i, t, ispalindrome):
                    result[t] = min(result[t], result[i]+1)
        return result[l]

    def palindrome(self, s, i, t, ispalindrome):
        if t-1-i < 1:
            ispalindrome[i][t-1] = True
            return True
    
        if s[i] != s[t-1]:
            ispalindrome[i][t-1] = False
            return False

        ispalindrome[i][t-1] = ispalindrome[i+1][t-2]
        return ispalindrome[i+1][t-2]