def pr(res,tt):
    print(f"Case #{tt+1}:",res)
    
t = int(input())
for tt in range(t):
    
    a,b = map(int,input().split())

    if not ((a-1)<=b<=(a*(a+1)//2-1)):
        pr("IMPOSSIBLE",tt)
        continue

    mcnt = list(range(a,2-1,-1))
    for i in range(1,len(mcnt)):
        mcnt[i] += mcnt[i-1]
    
    mcnt = [0]+mcnt
    rs = list(range(1,a+1))
    for i in range(len(mcnt)-2,-1,-1):
        if b<=mcnt[i]:
            b-=1
            continue
        else:
            j = i+(b-mcnt[i]-1)
            rs = rs[:i]+list(reversed(rs[i:j+1]))+rs[j+1:]
            b=mcnt[i]
    pr(' '.join(map(str,rs)),tt)