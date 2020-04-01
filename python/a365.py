class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        g = self.gcd(x, y)
        #这里无意中解决了0的情况
        return self.gcd(g, z) == g

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b%a, a)
