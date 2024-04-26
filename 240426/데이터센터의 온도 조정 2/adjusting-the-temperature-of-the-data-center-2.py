def solution():
    N,C,G,H = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    answer = 0
    for temp in range(0, 1001):
        sum_res = 0
        for i in range(N):
            sum_res += get_work(arr[i][0], arr[i][1], C,G,H, temp)
        answer = max(answer, sum_res)    
    print(answer)
def get_work(Ta, Tb, C,G,H, temp):
    if temp < Ta:
        return C
    if Ta <= temp <= Tb:
        return G
    if temp > Tb:
        return H
solution()