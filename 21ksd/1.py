from collections import Counter

def chk(rs):
    cnt = 0
    x,y,z = rs[0]
    if z-y==y-x: cnt+=1
    x,y,z = [rs[i][0] for i in range(3)]
    if z-y==y-x: cnt+=1
    x,y,z = rs[2]
    if z-y==y-x: cnt+=1
    x,y,z = [rs[i][2] for i in range(3)]
    if z-y==y-x: cnt+=1
    return cnt

def go(rs):
    pr = chk(rs)
    ns = []
    ns.append(rs[0][0]+rs[2][2])
    ns.append(rs[0][1]+rs[2][1])
    ns.append(rs[0][2]+rs[2][0])
    ns.append(rs[1][0]+rs[1][2])
    ss = list(Counter(ns).items())
    ss.sort(reverse=True,key=(lambda x:x[1]))
    mx = 0
    for x,y in ss:
        if x%2!=0: continue
        if y>mx: mx = y

    return pr+mx

t = int(input())
for ti in range(t):
    r1 = list(map(int,input().split()))
    r2 = list(map(int,input().split()))
    r2 = [r2[0],0,r2[1]]
    r3 = list(map(int,input().split()))
    res = go([r1,r2,r3])
    print(f"Case #{ti+1}: {res}")
    