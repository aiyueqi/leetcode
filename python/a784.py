from typing import *
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        self.f(0, "", len(S), S, result)
        return result

    def f(self, i, s, length, S, result):
        if i>= length:
            result.append(s)
            return
        
        self.f(i+1, s+S[i], length, S, result)
    
        if ord(S[i]) - ord('0') < 10:
            return
        
        diff = ord('a') - ord('A')
        if ord(S[i]) - ord('A') < 26:
            self.f(i+1, s+chr(ord(S[i]) + diff), length, S, result)
            return
        
        self.f(i+1, s+chr(ord(S[i]) - diff), length, S, result)
