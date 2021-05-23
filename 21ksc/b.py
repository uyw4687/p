t = int(input())
for i in range(1,t+1):
    g = int(input())
    
    cnt = 0
    sub = 0; ii = 1
    while True:
        cg = g-sub
        if cg<=0: break
        if cg%ii==0: cnt+=1
        sub+=ii; ii+=1

    print(f"Case #{i}: {cnt}")