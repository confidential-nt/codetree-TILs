def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x:(x[1], x[0]))

    answer = 0
    for i in range(1, n):
        if arr[i][1] == arr[i - 1][1]:
            continue
        answer += arr[i - 1][0]
        
    
    answer += arr[-1][0]

    print(answer)

solution()