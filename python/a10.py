from typing import List, Dict, Tuple

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        p = p + " "
        #这里设置成m+1，为了使用p[-1]
        A = [[False] * (m+1) for i in range(0, 2)]
        #设置成除了*之外的都ok
        A[1][-1] = True

        #循环
        flag = 1 
        for i in range(0, n):
            flag = 1-flag
            print(A[flag])
            print(A[1-flag])
            for j in range(-1, m-1):
                index = j
                if not A[1-flag][index]:
                    continue
                if p[index] != "*" and index + 1 < m:
                    index += 1
                    A[flag][index] = self.letterMatch(s[i], p[index])
                elif p[index] == "*":
                    A[flag][index] = self.letterMatch(s[i], p[index]) 
                    while index<m and p[index] == "*":
                        index += 1
                    if index<m:
                        A[flag][index] = self.letterMatch(s[i], p[index])
                    
        #结尾
        index = m-1
        while index >= 0:
            if not A[flag][index]:
                index -= 1
                continue
            for i in range(index+1, m):
                if p[i] != "*":
                    return False
            return True
            
        return False

    def letterMatch(self, ss, pp):
        return pp == "." or ss == pp

test = Solution()
print(test.isMatch("aa","a*"))
