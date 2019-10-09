from typing import *

#超时了 O((m*n)^(距离))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lastset = {word1}
        def add(s, newset):
            for w in word2:
                for i in range(0, len(s)+1):
                    newset.add(s[:i] + w + s[i:])
        def replace(s, newset):
            for w in word2:
                for i in range(0, len(s)):
                    newset.add(s[:i] + w + s[i+1:])
        def remove(s, newset):
            for i in range(0, len(s)):
                newset.add(s[:i] + s[i+1:])

        def dp(lastset):
            if word2 in lastset:
                return 0 
            newset = set()
            for s in lastset:
                add(s, newset)
                replace(s, newset)
                remove(s, newset)
            return dp(newset) + 1
        return dp(lastset)

s = Solution()
print(s.minDistance("horse", "ros"))
            

