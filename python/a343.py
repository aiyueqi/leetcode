from typing import List, Dict, Tuple

#法一 动态规划
#class Solution:
#    record = None
#
#    def integerBreak(self, n: int) -> int:
#        if n<2:
#            return 0;
#        if n<4:
#            return n-1;
#
#        self.record = [0]*(n+1)
#
#        return self.f(n);
#
#    def f(self, n):
#        if n<5:
#            return n;
#        if self.record[n] != 0:
#            return self.record[n]
#
#        for i in range(1, n//2+1):
#            tmp = self.f(i)*self.f(n-i)
#            self.record[n] = max(self.record[n], tmp)
#        return self.record[n]

#法二 贪心
#n>=5时 3(n-3)>=2(n-2)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n<2:
            return 0
        if n<4:
            return n-1
        if n==4:
            return 4
        
        num = n//3
        mol = n%3

        if mol == 0:
            return 3**num
        elif mol == 1:
            return 3**(num-1)*4
        else:
            return 3**num*2

s = Solution()
print(s.integerBreak(10))

#测试用例
#边界 n=0~3
#正常值 n=4,5,9
#非法值 n=-1
