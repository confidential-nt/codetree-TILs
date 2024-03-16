def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            if j - i > 1:
                max_sum = max(max_sum, arr[i] + arr[j])
    print(max_sum)

solution()