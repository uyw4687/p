def gn(i,j, h,c, dg):
    rs = []
    if 0<=i-1: rs.append((i-1,j))
    if i+1<h: rs.append((i+1,j))
    if 0<=j-1: rs.append((i,j-1))
    if j+1<c: rs.append((i,j+1))

    if dg:
        if 0<=i-1 and 0<=j-1: rs.append((i-1,j-1))
        if 0<=i-1 and j+1<c: rs.append((i-1,j+1))
        if i+1<h and 0<=j-1: rs.append((i+1,j-1))
        if i+1<h and j+1<c: rs.append((i+1,j+1))

    return rs

def gn2(i,j, h,c):
    rs = []
    if 0<=i-1: rs.append((i-1,j))
    if i+1<h: rs.append((i+1,j))
    if 0<=j-1: rs.append((i,j-1))
    if j+1<c: rs.append((i,j+1))

    return rs

def go(i,j,im,done, h,c, dg):
    for x,y in gn(i,j, h,c, dg):
        if done[x][y]: continue
        if im[x][y]==0: continue
        else: done[x][y]=True; go(x,y,im,done, h,c, dg)

def solution(im):
    h,c = len(im),len(im[0])
    done = [[False]*c for _ in range(h)]
    rs = []
    cnt = 0
    for i in range(h):
        for j in range(c):
            if im[i][j]==0: continue
            if not done[i][j]: cnt+=1; go(i,j,im,done, h,c, False)
    rs.append(cnt)

    done = [[False]*c for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(c):
            if im[i][j]==0: continue
            if not done[i][j]: cnt+=1; go(i,j,im,done, h,c, True)
    rs.append(cnt)
    return rs