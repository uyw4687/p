import sys
input=sys.stdin.readline
t,n=map(int,input().split())
mapping={'Mon':0,'Tue':1,"Wed":2,"Thu":3,"Fri":4}
total=0
for i in range(n):
  inf=input().split()
  total+=24*(mapping[inf[2]]-mapping[inf[0]])+int(inf[3])-int(inf[1])
if total>=t:
  print(0)
elif t-total>48:
  print(-1)
else:
  print(t-total)