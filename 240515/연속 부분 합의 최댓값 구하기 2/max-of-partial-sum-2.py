def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    sum_res = 0
    for i in range(n):
        sum_res += arr[i]
        if sum_res < 0 and i != n - 1:
            sum_res = 0
    print(sum_res)       


solution()