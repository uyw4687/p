from collections import Counter

def solution(inp_str):
    
    answer = []

    if not (8<=len(inp_str)<=15):
        answer.append(1)
    
    scs = set('~!@#$%^&*')
    
    aa = bb = cc = dd = ww = False
    
    for x in inp_str:
        if ord('A')<=ord(x)<=ord('Z'):
            aa = True
            continue
        if ord('a')<=ord(x)<=ord('z'):
            bb = True
            continue
        if ord('0')<=ord(x)<=ord('9'):
            cc = True
            continue
        if x in scs:
            dd = True
            continue
        if not ww:
            ww = True
            answer.append(2)
    
    cnt = 0
    for x in [aa,bb,cc,dd]:
        if x:
            cnt += 1
    if cnt < 3:
        answer.append(3)
    
    pv = inp_str[0]
    cs = 1
    for x in inp_str[1:]:
        if pv==x:
            cs += 1
            if cs>=4:
                answer.append(4)
                break
        else:
            cs = 1
            pv = x
    
    for x,y in Counter(inp_str).items():
        if y>=5:
            answer.append(5)
            break
    
    if len(answer)==0:
        answer.append(0)
    
    return answer