def solution():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N):
        for j in range(N - 2):
            for l in range(N):
                for k in range(N - 2):
                    if i == l and abs(j - k) < 3 :
                        continue
                    count1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                    count2 = arr[l][k] + arr[l][k + 1] + arr[l][k + 2]
                    
                    max_count = max(max_count, count1 + count2)
    print(max_count)


   
solution()