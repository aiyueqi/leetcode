#法一：O(n*2) 超时
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        length = len(nums)
        for i in range(length):
            count = 0
            for j in range(i, length):
                if count == k:
                    result += 1
                count += nums[j]%2
            if count == k:
                result += 1
        return result

#法二：O(n)

