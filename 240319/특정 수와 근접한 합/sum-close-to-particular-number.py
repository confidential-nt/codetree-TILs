def solution():
    N,S = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = float("inf")
    for i in range(N):
        for j in range(i+1,N):
            sum_arr = arr[:]
            sum_arr[i] = 0
            sum_arr[j] = 0
            
            sum_result = sum(sum_arr)
            
            answer = min(answer, abs(S - sum_result))
    print(answer)
solution()