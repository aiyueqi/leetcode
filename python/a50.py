from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        e = (n > 0) and n or -n 

        result = 1
        tmp = x
        while e!=0:
            if e&1 !=0:
                result*=tmp
            e = e>>1
            tmp = tmp*tmp

        if n>0:
        	return result
        else:
        	return 1.0/result

s = Solution()
print(s.myPow(0.00001, 2147483647))
