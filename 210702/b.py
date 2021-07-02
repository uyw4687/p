def solution(a, b):
    res = a%(10**5)
    for _ in range(b-1):
        res = (res*a)%(10**5)
    return res