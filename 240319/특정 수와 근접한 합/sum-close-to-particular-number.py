def solution():
    N,S = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_sum = sum(arr)
    answer = float("inf")
    for i in range(N):
        for j in range(i+1,N):
            
            sum_result = arr_sum - arr[i]- arr[j]
            
            answer = min(answer, abs(S - sum_result))
    print(answer)
solution()