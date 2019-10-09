from typing import *

# O((m*n)^(距离/2))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lastset1 = {word1}
        lastset2 = {word2}
        def add(s, newset, word):
            for w in word:
                for i in range(0, len(s)+1):
                    newset.add(s[:i] + w + s[i:])
        def replace(s, newset, word):
            for w in word:
                for i in range(0, len(s)):
                    newset.add(s[:i] + w + s[i+1:])
        def remove(s, newset, word):
            for i in range(0, len(s)):
                newset.add(s[:i] + s[i+1:])

        def dp(word, lastset1, lastset2):
            if len(lastset1 & lastset2) != 0:
                return 0
            newset = set()
            if word == word2:
                for s in lastset1:
                    add(s, newset, word)
                    replace(s, newset, word)
                    remove(s, newset, word)
                lastset1 = newset
                return dp(word1, lastset1, lastset2) + 1
            else:
                for s in lastset2:
                    add(s, newset, word)
                    replace(s, newset, word)
                    remove(s, newset, word)
                lastset2 = newset
                return dp(word2, lastset1, lastset2) + 1
        return dp(word1, lastset1, lastset2)

s = Solution()
print(s.minDistance("algorithm", "altruistic"))

