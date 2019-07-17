class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        result = [[None]*l for i in range(l)]
        start = 0
        end = -1
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if i==j:
                    result[i][j] = True
                    continue
                if s[i] != s[j]:
                    result[i][j] = False
                    continue
                if i+1 > j-1:
                    result[i][j] = True
                    continue
                result[i][j] = result[i+1][j-1]

        for i in range(0, l):
            for j in range(i, l):
                if result[i][j]:
                    if end - start < j - i:
                        end = j
                        start = i

        # print(result)
        # print(s[start: end+1])
        return s[start: end+1] 
