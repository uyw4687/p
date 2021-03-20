def solution(enter, leave):

    ll = len(leave)

    cs = [0]*(ll+1)
    x = set()

    i = -1
    for j in range(ll):
        cl = leave[j]
        while cl not in x:
            i+=1
            x.add(enter[i])
        x.remove(cl)
        cs[cl] += len(x)
        for xx in x:
            cs[xx] += 1

    answer = cs[1:]
    return answer