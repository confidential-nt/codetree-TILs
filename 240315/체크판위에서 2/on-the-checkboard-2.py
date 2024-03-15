def solution():
    R,C = map(int, input().split())
    arr = [input().split() for _ in range(R)]
    start = arr[0][0]
    end = arr[R -1][C - 1]
    loc = (0,0)
    count = 0
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            for k in range(i+1, R - 1):
                for l in range(j+1, C - 1):
                    if arr[i][j] != start and arr[k][l] != end and arr[i][j] != arr[k][l]:
                        count += 1
                        
    print(count)









solution()