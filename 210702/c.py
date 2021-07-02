from math import factorial as ft
def solution(n, m):
    answer = int(ft(n+m)/ft(n)/ft(m))
    return answer