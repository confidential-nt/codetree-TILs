def solution():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    for i in range(n - k + 1):
        sum_res = 0
        for j in range(i, i+k):
            sum_res += arr[j]
        answer = max(answer, sum_res)    
    print(answer)

solution()