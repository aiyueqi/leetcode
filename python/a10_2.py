from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        A = [[False for i in range(0, m+1)] for j in range(0,2) ]
        A[1][0] = m>0 and p[0]!='*'
        flag = 1

        for i in range(0, n):
            flag = 1-flag
            for j in range(0, m+1):
                A[flag][j] = False
            for j in range(0, m):
                if A[1-flag][j] == False:
                    continue
                index = j
                #TODO 
                while True:
                    if j+1 == m or p[j+1] != "*":
                        A[flag][j+1] = A[flag][j+1] or self.success(s[i], p[j])
                        continue
                index = j
                while: 
                    index<m 
                #初始化的时候处理p，使得没有两个相连的*
                else:
                    A[flag][j] = self.success(s[i], p[j])
                    index = j+1
                    while index<m and p[index]=='*':
                        index += 1
                    A[flag][index] = index == m or self.success(s[i], p[index])
            print(A[flag])
                    
        return A[flag][m] or m-1>=0 and A[flag][m-1] and p[m-1] != "*"

    def success(self, ss, pp):
        if pp == '.':
            return True
        return ss == pp

s = Solution()
print(s.isMatch("mississippi", "mis*is*ip*."))
