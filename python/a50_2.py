from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n

        #0^0 = 1
        result = 1
        tmp = x
        while n!=0:
            if n&1 !=0:
                result*=tmp
            n = n>>1
            tmp *= tmp
        return result

s = Solution()
print(s.myPow(0.00001, 2147483647))
