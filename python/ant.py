import copy
def antTree():

    #m行n列
    m = 3
    n = 4
    result = []
    tmp = [[0 for i in range(n)] for j in range(m)]
    num = 3
    mmax = [0]

    def f(row, col):
        if row == m:
#            print("end row=", row, "col=", col)
            if checkResult():
                t = calTotal()
                if t > mmax[0]:
                    mmax[0] = t
                    result.clear()
                    result.append(copy.deepcopy(tmp))
                if t == mmax[0]:
                    result.append(copy.deepcopy(tmp))
            return

        if col == n:
            f(row+1, 0)
            return

        tmp[row][col] = 0
        f(row, col+1)
        tmp[row][col] = 1
        f(row, col+1)

    def printResult(tmp):
        for i in range(0, m):
            for j in range(0, n):
                print(tmp[i][j], end=" ")
            print()
        print()

    def calTotal():
        total = 0
        for i in range(0, m):
            for j in range(0, n):
                if tmp[i][j]:
                    total += 1
        return total

    def checkResult():
        flag = help(0, 0, 0, fRow)
        flag = flag and help(0, 0, 0, fCol)
        flag = flag and help(0, 0, 0, fRightBias)
        flag = flag and help(0, n-1, 0, fLeftBias)
        return flag

    def help(i, j, count, f):
        #约定i=-1表示结束
        if i == -1:
            return True

        if tmp[i][j] == 1:
            count += 1
            if count >= num:
                return False

            next_i, next_j, count = f(i, j, count)
            return help(next_i, next_j, count, f)

        else:
            next_i, next_j, count = f(i, j, count)
            return help(next_i, next_j, 0, f)


    def fRow(i, j, count):
        if i == m-1 and j == n-1:
            return -1, -1, count
        if j == n-1:
            return i+1, 0, 0
        return i, j+1, count

    def fCol(i, j, count):
        if i == m-1 and j == n-1:
            return -1, -1, count
        if i == m-1:
            return 0, j+1, 0
        return i+1, j, count

    #由n=3 num=3可以只扫第一行
    def fRightBias(i, j, count):
        if i == 0 and j == n-1:
            return -1, -1, count
        diff = j - i
        if i == m-1 or j == n-1:
            return 0, diff+1, 0
        return i+1, j+1, count

    def fLeftBias(i, j, count):
        if i == 0 and j == 0:
            return -1, -1, count
        diff = i+j
        if i == m-1 or j == 0:
            return 0, diff-1, 0
        return i+1, j-1, count
        
    f(0, 0)
    print("最多可种的树的棵树为：", mmax[0])
    length = len(result)
    print("共有", length,"种种树方法")
    for i in range(length):
        print("种法", i+1, ":")
        printResult(result[i])

antTree()
