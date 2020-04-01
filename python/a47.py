from typing import *

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 0:
#             return []

#         length = len(nums)
#         nums.sort()
#         num = []
#         counts = []
#         count = 1
#         for i in range(0, length - 1):
#             if nums[i] == nums[i+1]:
#                 count += 1
#                 continue
#             num.append(nums[i])
#             counts.append(count)
#             count = 1

#         counts.append(count)
#         num.append(nums[length-1])

#         result = []
#         mark = [False] * length
#         tmp = [0] * length
#         self.f(0, 0, 0, tmp, mark, counts, num, len(counts), length, result)


#         return result

#     def f(self, index, n, start, tmp, mark, counts, num, counts_length, nums_length, result):
#         #print("index=", index, "n=", n)
#         if n == counts[index] :
#             if counts_length-1  == index:
#                 result.append(tmp.copy())
#                 return
#             self.f(index+1, 0, 0, tmp, mark, counts, num, counts_length, nums_length, result)
#             return
#         # i = [n, nums_length-1-(count[index]-1-n)]
#         for i in range(start, nums_length-counts[index]+n+1):
#             if mark[i]:
#                 continue
#             mark[i] = True
#             tmp[i] = num[index]
#             self.f(index, n+1, i+1, tmp, mark, counts, num, counts_length, nums_length, result)
#             mark[i] = False

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 数组先排序
        self.res = []
        self.recur(nums,[])
        return self.res

    def recur(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue
            self.recur(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用。


#没明白正确性
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
            print(ans)
        return ans

s = Solution()
print(s.permuteUnique([2,1,3,1]))
