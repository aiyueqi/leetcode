from typing import List, Dict, Tuple

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        A = [[False] * m for i in range(0, n)]
        #初始化
        if(len(A) >0 and len(A[0])>0):
            A[0][0] = True

        #循环
        for i in range(1, n):
            for j in range(0, m):
                index = A[i-1][j]
                if not index:
                    continue
                if p[index] != "*" and index + 1 < m:
                    index += 1
                    A[i][index] = self.letterMatch(s[i], p[index])
                elif p[index] == "*":
                    A[i][index] = self.letterMatch(s[i], p[index]) 
                    while index<m and p[index] == "*":
                        index += 1
                    if index<m:
                        A[i][index] = self.letterMatch(s[i], p[index])
                    
        #结尾
        index = m-1
        while index >= 0:
            if not A[n-1][index]:
                continue
            for i in range(index+1, m):
                if p[i] != "*":
                    return False
            return True
            
        return False

    def letterMatch(self, ss, pp):
        return pp == "." or ss == pp

test = Solution()
print(test.isMatch("aa","bb"))
