t,n,q = map(int,input().split())
for _ in range(t):
    print(1,2,3)
    cl = [1,2,3]
    res = int(input())
    cl.remove(res)
    cl.insert(1,res)

    for nri in range(4,n+1):
        l = -1
        r = len(cl)-1
        rm = len(cl)-1
        while True:
            c = (l+r)//2
            print(cl[c],cl[rm],nri)
            res = int(input())
            
            if res==cl[rm]:
                cl.append(nri)
                break
            elif res==nri:
                l = c
            else:
                r = c

            assert(l+1<=r)
            if r-l==1:
                cl = cl[:r]+[nri]+cl[r:]
                break

    print(' '.join(map(str,cl)))
    if int(input())==1:
        continue
    else:
        break