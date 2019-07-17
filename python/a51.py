from typing import List, Dict, Tuple

class Solution:
    global a
    global result
    a = [0] * 100
    result = []
    
    def f(self, row, n):
        global a
        global result
        if row == n:
            result.append(self.plot(n))
            return
        for col in range(0, n):
            a[row] = col
            if not self.check(row, col, n):
                continue
            self.f(row+1, n)

    def plot(self, n):
        global a
        picture = []
        s = ""
        for i in range(0, n):
            for j in range(0, n):
                if a[i] == j:
                    s += 'Q'
                else:
                    s += '.'
            picture.append(s)
            s=""
        return picture

    def check(self, row, col, n):
        global a
        for i in range(0, row):
            if a[i] == col:
                return False
    #        print("i="+str(i)+" a[i]="+str(a[i])+" row"+str(row)+" col"+str(col)+" a[i]+row-i="+str((a[i]+row-i)%n)+'\n')
            if a[i] + row-i == col:
                return False
            if col + row-i == a[i]:
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        global result
        result = []
        self.f(0, n)
        return result