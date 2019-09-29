from typing import *

# 遍历p，与s作比较
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
                self.loop(lastset, newset, p[i], s, True, m)

            else:
                #匹配一个
                self.loop(lastset, newset, p[i], s, False, m)
            lastset = newset
            print(lastset)
        return m-1 in lastset

    def loop(self, lastset, newset, pp, s, star, m):
        for j in lastset:
            index = j+1
            if index >= m:
                continue
            if star:
                while index<m and self.match(s[index], pp):
                    newset.add(index)
                    index += 1
            else:
                if self.match(s[index], pp):
                    newset.add(index)

    def match(self, ss, pp):
        if pp == '.':
            return True
        return ss == pp

s = Solution()
print(s.isMatch("mississippi", "mis*is*ip*."))
