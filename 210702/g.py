from collections import deque
def solution(N, relation, dirname):
    n = N; rl = relation; dn = [0]+[len(x) for x in dirname]
    ps = [-1]*(n+1)
    cs = [0]*(n+1)
    ms = [0]*(n+1)
    for a,b in rl: ps[b]=a; cs[a]+=1
    ls = deque([i for i in range(1,n+1) if cs[i]==0])
    while len(ls)!=0:
        x = ls.popleft()
        print(x)
        if cs[x]!=0: continue
        if x==1: continue
        cs[ps[x]]-=1
        ms[ps[x]] = max(ms[ps[x]], dn[x]+ms[x]+1)
        ls.append(ps[x])

    return dn[1]+ms[1]

    print(ps)