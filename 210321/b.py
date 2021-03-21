def get_matrices(r,c,ma,right,left,down,up):
    for i in range(r):
        cnt = 0
        for j in range(c):
            if ma[i][j]==0:
                cnt = 0
            else:
                cnt += 1
                left[i][j] = cnt

    for i in range(r):
        cnt = 0
        for j in range(c-1,-1,-1):
            if ma[i][j]==0:
                cnt = 0
            else:
                cnt += 1
                right[i][j] = cnt

    for j in range(c):
        cnt = 0
        for i in range(r):
            if ma[i][j]==0:
                cnt = 0
            else:
                cnt += 1
                up[i][j] = cnt

    for j in range(c):
        cnt = 0
        for i in range(r-1,-1,-1):
            if ma[i][j]==0:
                cnt = 0
            else:
                cnt += 1
                down[i][j] = cnt

t = int(input())

for n in range(t):
    
    r,c = map(int,input().split())
    right = [[0]*c for _ in range(r)]
    left = [[0]*c for _ in range(r)]
    down = [[0]*c for _ in range(r)]
    up = [[0]*c for _ in range(r)]
    
    ma = []
    for _ in range(r):
        ma.append(list(map(int,input().split())))
    
    get_matrices(r,c,ma,right,left,down,up)
    infos = [right,left,down,up]

    cnt = 0
    for i in range(r):
        for j in range(c):
            ps = []
            ps.append([right[i][j],down[i][j]])
            ps.append([right[i][j],up[i][j]])
            ps.append([left[i][j],down[i][j]])
            ps.append([left[i][j],up[i][j]])
            for x in ps:
                x.sort()
            for x,y in ps:
                if x<=1:
                    continue
                cnt += max(0,min(x,y//2)-1)
                cnt += max(0,min(y,x//2)-1)
    
    print(f"Case #{n+1}:",cnt)