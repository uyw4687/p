def solution(ip_addrs, langs, scores):
    cnt = {}

    for x in ip_addrs:
        if x not in cnt: cnt[x] = 1
        else: cnt[x]+=1

    al = sorted(zip(ip_addrs, langs, scores), key=(lambda x:x[0]))

    i=0
    gct = 0
    while i<len(al):
        curr = [al[i]]
        cuip = al[i][0]
        i+=1
        while i<len(al):
            if al[i][0]!=cuip: break    
            curr.append(al[i])
            i+=1
        if len(curr)>=4: continue
        elif len(curr)==1: gct+=1; continue
        elif len(curr)==3:
            a,b,c = [x[1] for x in curr]
            if (('C' in a) and ('C' in b) and ('C' in c)): continue
            if a==b==c: continue
            gct+=3
        elif len(curr)==2:
            a,b = [x[1] for x in curr]
            if a!=b: gct+=2; continue
            a,b = [x[2] for x in curr]
            if a!=b: gct+=2; continue

    return gct