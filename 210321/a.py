def get_score(curr_str,n):
    total = 0
    for i in range(n//2):
        if curr_str[i]!=curr_str[n-1-i]:
            total += 1
    return total

t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    curr_str = input()
    score = get_score(curr_str,n)
    print(f"Case #{i+1}:",abs(k-score))