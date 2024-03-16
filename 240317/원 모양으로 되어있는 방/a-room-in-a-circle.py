def solution():
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    min_dist = float("inf")
    for i in range(N):
        sum_dist = 0
        for j in range(N):
            dist = (j + N - i) % N # 이렇게하면 부호 판단 안해도 됨 
            sum_dist += (dist) * arr[j]
        min_dist = min(min_dist, sum_dist)
    print(min_dist)


solution()