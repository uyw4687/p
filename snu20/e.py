import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))

prob=[1/x[0]]*x[0]
eind=x[0]
minp=x[0]

for i in range(1,n):
  if x[i]>=minp:
    continue
  minp=x[i]
  for j in range(minp,eind):
    prob[j%minp]+=prob[j]
  eind=minp
  
res=0
for i in range(eind):
  res+=(i*prob[i])
print(res)