class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length = len(word2)
        def f(n, tmp, result):
            tmpLen = len(tmp)
            if n == length:
                #末尾全部删除
                return result + tmpLen
            if tmpLen == 0:
                #直接剪枝, 末尾全部添加
                return result + length - n
            if tmp[0] == word2[n]:
                return f(n+1, tmp[1:], result)
            #依次为修改，添加，删除
            return min(f(n+1, tmp[1:], result+1), f(n, tmp[1:], result+1), f(n+1, tmp[0:], result+1))
        return f(0, word1, 0)
