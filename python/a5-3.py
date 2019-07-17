from typing import List, Dict, Tuple

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        result = [[True]*l for i in range(2)]
        start = 0
        end = -1
        line = 0
        for i in range(l-1, -1, -1):
            line = 1-line
            for j in range(i, l):
                if i==j:
                    result[line][j] = True
                elif s[i] != s[j]:
                    result[line][j] = False
                else:
                    result[line][j] = result[1-line][j-1]
                    
                if(result[line][j]):
                    if end - start < j - i:
                        end = j
                        start = i

        # print(result)
        # print(s[start: end+1])
        return s[start: end+1] 
s = Solution()
# s.longestPalindrome("babad")
s.longestPalindrome("cbbd")
