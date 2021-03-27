def ev(c,a,b):
    cc = c[0]
    cost = {'C':a, 'J':b}
    tct = 0
    for i in range(1,lc):
        if cc != c[i]:
            tct += cost[cc]
            cc = c[i]
    
    return tct

def pr(res,tt):
    print(f"Case #{tt+1}:",res)

def fpos(c):
    i=0
    lc = len(c)
    while True:
        if i>=lc:
            break

        while c[i]!='?':
            i+=1
            if i>=lc:
                break
        if i>=lc:
            break
        
        if (i-1)>=0:
            c[i] = c[i-1]
            i += 1
        else:
            j = i+1
            while c[j]=='?':
                j+=1
            
            nch = c[j]
            c = [nch]*(j-1-0+1)+c[j:]
            i = j+1
    return c

def ftneg(c):
    oc = {'J':'C', 'C':'J'}

    i=0
    lc = len(c)
    while True:
        if i>=lc:
            break

        while c[i]!='?':
            i+=1
            if i>=lc:
                break
        if i>=lc:
            break
        
        if (i-1)>=0:
            c[i] = oc[c[i-1]]
            i += 1
        else:
            j = i+1
            while c[j]=='?':
                j+=1
            
            nch = [c[j],oc[c[j]]]
            ct = (j-1-0+1)
            cd = ct//2
            cx = ct%2
            c = ([oc[c[j]]]*cx)+(nch*cd)+c[j:]
            i = j+1
    return c

def fnegb(c,a,b):
    oc = {'J':'C', 'C':'J'}
    
    ech = lch = None
    if b>0:
        ech,lch = 'J','C'
    else:
        ech,lch = 'C','J'

    i=0
    lc = len(c)
    while True:
        if i>=lc:
            break

        while c[i]!='?':
            i+=1
            if i>=lc:
                break
        if i>=lc:
            break
        
        if (i-1)>=0:
            if (i+1)<lc:
                c[i] = oc[c[i-1]]
                i += 1
            else:
                c[i] = ech
                break
        else:
            j = i+1
            while c[j]=='?':
                j+=1
            
            nch = [c[j],oc[c[j]]]
            ct = (j-1-0+1)
            cd = ct//2
            cx = ct%2
            
            if c[j]==ech:
                fch = lch
            else:
                fch = c[j]

            c = ([fch]*cx)+(nch*cd)+c[j:]
            i = j+1
    return c

def fnegu(c,a,b):
    oc = {'J':'C', 'C':'J'}
    
    ech = lch = None
    if b>0:
        ech,lch = 'J','C'
    else:
        ech,lch = 'C','J'

    i=0
    lc = len(c)
    while True:
        if i>=lc:
            break

        while c[i]!='?':
            i+=1
            if i>=lc:
                break
        if i>=lc:
            break
        
        if (i-1)>=0:
            if (i+1)<lc:
                c[i] = c[i-1]
                i += 1
            else:
                c[i] = ech
                break
        else:
            j = i+1
            while c[j]=='?':
                j+=1

            ct = (j-1-0+1)
            c = ([lch]*ct)+c[j:]
            i = j+1
    return c
    
t = int(input())
for tt in range(t):
    a,b,c = input().split()
    a,b = map(int,(a,b))

    c = list(c)
    lc = len(c)

    mi = False
    if (a<0) or (b<0):
        mi = True

    if lc==1:
        pr(0,tt)
        continue

    if c==(['?']*lc):
        if not mi:
            pr(0,tt)
            continue
        if a>0 or b>0:
            if (a+b)>=0:
                pr(min(a,b),tt)
            else:
                pr((a+b)*(lc//2),tt)
        if a<=0 and b<=0:
            poss = lc-1
            tou = poss//2
            tod = poss-tou
            pr(max(a,b)*tou+min(a,b)*tod,tt)
        continue

    qin = False
    for i,x in enumerate(c):
        if x=='?':
            qin = True
            break

    if not qin:
        pr(ev(c,a,b),tt)
        continue
    
    # longer than 1
    # at least one question
    # at least one character
    if not mi:
        c = fpos(c)
    else:
        if (a<=0) and (b<=0):
            c = ftneg(c)
        
        # - + or + -
        elif a+b<=0:
            c = fnegb(c,a,b)
        else:
            c = fnegu(c,a,b)
    
    pr(ev(c,a,b),tt)
