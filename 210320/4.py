def solution(data, word):

    ld = len(data)
    its = [None]*(ld+1)
    prs = [-1]*(ld+1)
    cs = [0]*(ld+1)
    
    for x in data:
        a,b,c = x.split()
        a,c = map(int,[a,c])
        
        its[a] = b
        prs[a] = c
        
        cs[c] += 1
    
    # leaves
    ls = []
    for i,c in enumerate(cs):
        if c==0:
            ls.append(i)
    
    ll = len(ls)
    ps = [[] for _ in range(ll)]
    lw = len(word)
    
    for i,x in enumerate(ls):
        
        x = its[x]
        sx = 0
        ex = len(x)
            
        while True:
            r = x.find(word,sx,ex)
            if r==-1:
                break
            sx = r+lw

            ps[i].append(r)
    
    # by length
    nps = [[] for _ in range(20+1)]
    for i,x in enumerate(ps):
        nps[len(x)].append((i,x))
    ps = nps
    
    for i,x in enumerate(ps):
        for j in range(i-1,-1,-1):
            x.sort(key=(lambda x:x[1][j]))

    result = []
    
    nn = []
    for x in nps[1]:
        if x[1]==[0]:
            if len(its[ls[x[0]]])==lw:
                result.append(x[0])
                continue
        nn.append(x)
    
    nps[1] = nn

    for x in reversed(ps[1:]):
        lx = len(x)
        
        i = 0
        cis = []
        while i<lx:
            
            curr = x[i][1]
            cis.append(x[i][0])
            
            if i+1<lx:
                if curr==x[i+1][1]:
                    i+=1
                    continue
                else:
                    result.extend(cis)
                    cis = []
            else:
                result.extend(cis)
            i+=1
    
    nr = []
    for x in result:
        res = its[ls[x]]
        px = prs[ls[x]]
        while px!=0:
            res = its[px]+'/'+res
            px = prs[px]
        nr.append(res)
    if len(nr)==0:
        nr = [f"Your search for ({word}) didn't return any results"]

    return nr