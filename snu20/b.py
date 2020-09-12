import sys
input=sys.stdin.readline
import re
instr=input().rstrip()
res=re.split(" |-",instr)
ans=len(res)
left={'c','j','n','m','t','s','l','d'}
right={'a','e','i','o','u','h'}
for x in res:
  if len(x)<3:
    continue
  x=x[:4]
  if x[0] in left:
    if x[1]=="'" and x[2] in right:
      ans+=1
  elif x[:2]=='qu':
    if x[2]=="'" and x[3] in right:
      ans+=1
print(ans)