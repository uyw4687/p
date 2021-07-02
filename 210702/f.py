def gn(i,j, h,c):
    rs = []
    if 0<=i-1: rs.append((i-1,j))
    if i+1<h: rs.append((i+1,j))
    if 0<=j-1: rs.append((i,j-1))
    if j+1<c: rs.append((i,j+1))
    return rs

def go(b, i,j, v, l, u):
    cc = b[i][j]
    mv = l
    for x,y in gn(i,j, 5,5):
        if v[x][y]: continue
        if ord(b[x][y])==ord(cc): continue
        elif ord(b[x][y])<ord(cc):
            if u: continue
            v[x][y] = True
            mv = max(mv,go(b, x,y, v, l+1, True))
            v[x][y] = False
        else:
            v[x][y] = True
            mv = max(mv,go(b, x,y, v, l+1, u))
            v[x][y] = False

    return mv

def solution(board):
    mv = 0
    v = [[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            v[i][j] = True
            mv = max(mv,go(board, i,j, v, 1, False))
            v[i][j] = False

    return mv