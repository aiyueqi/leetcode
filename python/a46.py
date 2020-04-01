class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        mark = [False] * length
        tmp = []
        def f(i):
            if i == length:
                result.append(tmp.copy())
            
            for j in range(0, length):
                if mark[j]:
                    continue
                tmp.append(nums[j])
                mark[j] = True
                f(i+1)
                mark[j] = False
                tmp.pop()
        f(0)
        return result
