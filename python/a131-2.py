from typing import List, Dict, Tuple

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        self.memory = [0] * (n+1)
        self.memory[0] = [[]]
        return self.f(n, s)

    def f(self, t, s):
        if self.memory[t] != 0:
            return self.memory[t]
        tlist = []
        for i in range(0, t):
            if self.pandlindrome(s[i:t]):
                for j in self.f(i, s):
                    tmp = j[:]
                    tmp.append(s[i:t])
                    tlist.append(tmp)
        self.memory[t] = tlist
        return tlist

    def pandlindrome(self, s):
        return s == s[::-1]

