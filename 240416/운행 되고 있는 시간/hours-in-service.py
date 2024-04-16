def solution():
    n = int(input())
    times = [tuple(map(int, input().split())) for _ in range(n)]

    answer = 0

    for i in range(n):
        times_sum = [0] * (1001)
        for j in range(n):
            if i == j:
                continue
            for k in range(times[j][0], times[j][1]):
                times_sum[k] = 1   
        answer = max(answer, sum(times_sum))
    print(answer)    

solution()