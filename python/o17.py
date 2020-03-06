#打印从1到最大的n位数

class Solution:
    def printMaxN(self, n):
        s = [0] * n
        self.f(n, s, n)

    def f(self, n, s, nn):
        if n == 0:
            flag = False
            for i in range(nn-1, -1, -1):
                if s[i] != 0 or flag or i==0:
                    flag = True
                    print(s[i], end="")

            print("")
            return
        
        for i in range(0, 10):
            s[n-1] = i
            self.f(n-1, s, nn)

s = Solution()
s.printMaxN(4)

