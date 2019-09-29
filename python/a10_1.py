from typing import *

#遍历s，与p作比较
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        #下一个要匹配的p中的下标
        A = [[False] * (m+1) for i in range(0, 2)]
        A[1][0] = True

        flag = 1
        for i in range(0, n):
            flag = 1-flag
            for j in range(0, m+1):
                A[flag][j] = False
            for j in range(0, m):
                if A[1-flag][j] == False:
                    continue
                self.update(j, s[i], p, A, flag, m)
#            print(A[flag])

        #结尾是x*y*z*的情况
        if A[flag][m]:
            return True
        index = m-1
        while index>=0:
            if A[flag][index]:
                break
            index -= 1
        result = False
        while index>=0 and index<m:
            if index+1<m and p[index+1]=="*":
                result = True
                index += 2
            else:
                return False
        return result

    def update(self, j, ss, p, A, flag, m):
        if j >= m:
            return
        if j+1 == m or p[j+1] != "*":
            A[flag][j+1] = A[flag][j+1] or self.success(ss, p[j])
            return
        A[flag][j] = A[flag][j] or self.success(ss, p[j])
        self.update(j+2, ss, p, A, flag, m)

    def success(self, ss, pp):
        if pp == ".":
            return True
        return ss == pp

s = Solution()
print(s.isMatch("mississippi", "mis*is*p*."))
