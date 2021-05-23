MOD = 10**9+7
def res(s,n,k):
    vl = (n-1)//2

    total = 0
    mul = 1
    for i in range(vl,-1,-1):
        total = (total+((ord(s[i])-ord('a'))*mul)%MOD)%MOD
        mul = (mul*k)%MOD

    for i in range(vl,-1,-1):
        if s[i]==s[n-1-i]: continue
        if s[i]<s[n-1-i]:
            total += 1
        break
    return total%MOD
    
t = int(input())
for i in range(1,t+1):
    n,k = map(int,input().split())
    s = list(input())
    print(f"Case #{i}: {res(s,n,k)}")