class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def f(l, r, tmp):
            if l < 0 or r < 0:
                return
            if l > r:
                return
            if l == 0 and r == 0:
                result.append(tmp)
                return
            f(l-1, r, tmp+"(")
            f(l, r-1, tmp+")")
        f(n, n, "")
        return result
