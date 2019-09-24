from typing import List, Dict, Tuple

class Solution:

    column = set() 
    diagonal = set()
    diagonal2 = set()
    result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        A = [0] * n
        self.f(0, n, A)
        return self.result

    def addResult(self, n, A):
        tmp = [["."] * n for i in range(0, n)]
        for i in range(0, n):
            tmp[i][A[i]] = 'Q'
            tmp[i] = "".join(tmp[i])
        self.result.append(tmp)

    def f(self, i, n, A):
        if(i == n):
            self.addResult(n, A)
        for j in range(0, n):
            if(not self.check(i, j)):
                continue
            A[i] = j
            self.addSets(i, j)
            self.f(i+1, n, A)
            self.removeSets(i, j)

    def removeSets(self, i, j):
        self.column.remove(j)
        self.diagonal.remove(i-j)
        self.diagonal2.remove(i+j)

    def addSets(self, i, j):
        self.column.add(j)
        self.diagonal.add(i-j)
        self.diagonal2.add(i+j)

    def check(self, i, j):
        if j in self.column:
            return False
        if i-j in self.diagonal:
            return False
        if i+j in self.diagonal2:
            return False
        return True
        
s = Solution()
print(s.solveNQueens(1))
