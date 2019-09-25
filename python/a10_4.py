from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        lastset = {-1}

        for i in range(0, n):
            if p[i] == "*":
                continue
            newset = set()
            if (i+1)<n and p[i+1] == '*':
                #匹配多个
                newset = lastset.copy()
                for j in lastset:
                    index = j+1
                    if index>=m:
                        continue

                    while index<m and self.match(s[index], p[i]):
                        newset.add(index)
                        index += 1

            else:
                #匹配一个
                for j in lastset:
                    index = j+1
                    if index >= m:
                        continue
                    if self.match(p[i], s[index]):
                        newset.add(index)
            lastset = newset
            print(lastset)
        return m-1 in lastset

    def match(self, ss, pp):
        if pp == '.':
            return True
        return ss == pp
                

s = Solution()
print(s.isMatch("mississippi", "mis*is*ip*."))
