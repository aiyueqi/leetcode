from typing import *

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.f(postorder, 0, len(postorder)-1)

    def f(self, A, l, r):
        if r <= l:
           return True 
        bigger = -1
        for i in range(l, r):
            if bigger != -1 and A[i]<A[r]:
                return False
            if bigger == -1 and A[i]>A[r]:
                bigger = i
        if bigger == -1:
            return self.f(A, l, r-1)
        return self.f(A, l, bigger-1) and self.f(A, bigger, r-1)

