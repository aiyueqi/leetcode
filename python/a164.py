from typing import List, Dict, Tuple
from math import *

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0;
        mmax = max(nums)
        mmin = min(nums)
        size = ceil((mmax-mmin)/(n-1))
        if size == 0:
            return 0

        result = size
        bucket = [[-1, -1] for i in range(0,n)]

        #把最小值和最大值放到桶里
        for i in nums:
            index = (i-mmin)//size
            bucket[index][1] = max(bucket[index][1], i)
            if bucket[index][0] == -1:
                bucket[index][0] = i
            else:
                bucket[index][0] = min(bucket[index][0], i)

        #读桶
        l = mmin
        r = mmin
        for i in range(0, n-1):
            if bucket[i][1] != -1:
                l = bucket[i][1]
            if bucket[i+1][0] != -1:
                r = bucket[i+1][0]
                result = max(result, r-l)
        return result
        
s = Solution()
print(s.maximumGap([10]))
