from typing import List, Dict, Tuple

class Solution:
    class Solution:   
    def sqrt(self, x, l, r):
        if l>r:
            return min(l,r)
        n = (l+r)//2
        if n*n == x:
            return n
        if n*n < x:
            return self.sqrt(x, n+1, r)
        return self.sqrt(x, l, n-1)
    
    def mySqrt(self, x: int) -> int:
        return self.sqrt(x, 0, x)
        # l = 0
        # r = x
        # while(l<=r):
        #     n = (l+r)//2
        #     if n*n == x:
        #         return n
        #     if n*n < x:
        #         l = n+1
        #         continue
        #     r = n-1
        # return min(l, r)