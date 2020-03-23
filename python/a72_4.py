class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)

        result = [[None for i in range(length1+1)] for j in range(length2+1)]
        result[0][0] = 0

        def checkAndChange(i, j, p, q, add):
            if p > length2 or q > length1:
                return
            if result[p][q] == None:
                result[p][q] = result[i][j] + add
                return
            result[p][q] = min(result[p][q], result[i][j] + add)

        for i in range(0, length2):
            for j in range(0, length1):
                if result[i][j] == None:
                    continue
                if word2[i] == word1[j]:
                    checkAndChange(i, j, i+1, j+1, 0)
                    continue
                #添加
                checkAndChange(i, j, i+1, j, 1)
                #删除
                checkAndChange(i, j, i, j+1, 1)
                #修改
                checkAndChange(i, j, i+1, j+1, 1)
        mmin = None
        for i in range(0, length1+1):
            if result[length2][i] == None:
                continue
            now = result[length2][i] + length1 - i
            if mmin == None:
                mmin = now
            mmin = min(mmin, now)

        for i in range(0, length2+1):
            if result[i][length1] == None:
                continue
            now = result[i][length1] + length2 - i
            if mmin == None:
                mmin = now
            mmin = min(mmin, now)

        return mmin
s = Solution()
print(s.minDistance("a", "ab"))
