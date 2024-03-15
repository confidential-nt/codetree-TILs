def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(N - 2):
            count = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
            max_count = max(count, max_count)
    print(max_count)




solution()