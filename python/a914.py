class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {}
        for value in deck:
            if value in d:
                d[value] += 1
            else:
                d[value] = 1
        
        result = -1
        for key in d:
            if result == -1:
                result = d[key]
            result = self.gcd(result, d[key])
        return result >= 2
    
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b%a, a)
