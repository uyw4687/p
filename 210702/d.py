import sys
sys.setrecursionlimit(10**6)

def rt(p,i):
    if p[i]==-1: return i
    p[i] = rt(p,p[i])
    return p[i]

def solution(p, b):
    n = len(p)
    res = []
    cnt = [1]*n
    for i in range(n): rt(p,i)
    for x in p:
        if x==-1: continue
        cnt[x]+=1

    for x in b:
        if p[x]!=-1: res.append(0); continue
        res.append(cnt[x])

    return res