def cal(a, b, f):
    result = f(a, b)
    print(result)

def f(a, b):
    return a+b

cal(1,2, f)
