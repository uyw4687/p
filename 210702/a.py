def calc(x,y,op):
    if op=='+':
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y

def solution(s, op):
    res = []
    for i in range(len(s)-1):
        x,y = s[:i+1],s[i+1:]
        res.append(calc(int(x),int(y),op))

    return res