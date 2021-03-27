t = int(input())
for ii in range(t):
    
    cnt = 0
    n = int(input())
    ns = list(map(int,input().split()))
    for i in range(n-1):
        mj = i
        for j in range(i,n):
            if ns[mj]>ns[j]:
                mj = j
        ns = ns[:i]+list(reversed(ns[i:mj+1]))+ns[mj+1:]
        cnt += (mj-i+1)

    print(f"Case #{ii+1}:", cnt)
