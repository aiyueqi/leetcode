from typing import List, Dict, Tuple

#此题选取参照点时，可选取首或尾，但是考虑到数组未旋转的情况，如果选首需要特殊处理，选尾逻辑可以统一，故选择尾

#不考虑有重复数字的情况，有重复数字会有问题

#递归
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.f(0, len(nums)-1, nums)

    def f(self, l, r, A):
        if l>r:
            return None
        if l == r:
            return A[l]

        index = (l+r)//2
        if A[index] >= A[len(A) - 1]:
            return self.f(index+1, r, A)
        else:
            return self.f(l, index, A)

#s = Solution()
#print(s.findMin([]))

#循环
#class Solution:
#    def findMin(self, nums: List[int]) -> int:
#        l = 0
#        r = len(nums) - 1
#
#        if l>r:
#            return None
#        while l<r:
#            index = (l+r)//2
#            if nums[index] >= nums[len(nums) - 1]:
#                l = index+1
#            else:
#                r = index
#        return nums[l]

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([]))
print(s.findMin([5]))
print(s.findMin([5,5,5,5,5]))
print(s.findMin([1,3,3]))


