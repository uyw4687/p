def go(a,b,cost,xs):
    if len(xs)==0:
        return cost-a
    if len(xs)==1:
        return cost+xs.pop()
    return min(go(a,b,cost+xs[1]+b+b+a,xs[2:]),go(a,b,cost+xs[0]+a,xs[1:]))
    
def main():
    t = int(input())
    for ti in range(t):
        n = int(input())
        xs = list(map(int,input().split()))
        xs.sort()
        
        res = 0
        if n<=2: res = xs[-1]
        else:
            res = go(xs[0],xs[1],xs[1]+xs[0],xs[2:])

        print(f"#{ti+1}:",res)
        
main()
