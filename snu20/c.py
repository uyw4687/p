import sys
input=sys.stdin.readline
n,q=map(int,input().split())
a=list(map(int,input().split()))
vs=[a[0]]
inds=[0]
for i,v in enumerate(a):
  if v!=vs[-1]:
    vs.append(v)
    inds.append(i)
lenvs=len(vs)

def binary(a,b,x):
  if a==b:
    return a
  c=int((a+b)/2)
  if vs[c]<x:
    return binary(a,c,x)
  else:
    return binary(c+1,b,x)

maxa=a[0]
mina=a[n-1]

for i in range(q):
  x,y=map(int,input().split())
  res=max(0,a[y-1]-(x-1))
  if x<=mina:
    res+=(n-(y-1))
  elif x<=maxa:
    ind=binary(0,lenvs-1,x)
    res+=(inds[ind]-(y-1))
  print(max(0,res-1))
