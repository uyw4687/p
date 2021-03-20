def solution(table, languages, preference):

    names = []
    ords = []
    for x in table:
        x = x.split()
        names.append(x[0])
        ords.append(x[1:])

    rs = [0]*5
    for i,x in enumerate(languages):
        cp = preference[i]
        for ni in range(5):
            for j in range(0,4+1):
                if ords[ni][j]==x:
                    rs[ni]+=((5-j)*cp)

    mv = -1
    ns = []
    for i,x in enumerate(rs):
        if rs[i]>mv:
            mv = rs[i]
            ns = [names[i]]
        elif rs[i]==mv:
            ns.append(names[i])
    
    ns.sort()
    return ns[0]
