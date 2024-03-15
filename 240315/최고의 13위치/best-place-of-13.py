def solution():
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    max_count = 0
    for i in range(N):
        for j in range(N):
            di = i
            dj = j + 2
            if 0 <= di < N and 0 <= dj < N:
                result = matrix[di][j:dj+1].count(1)
                max_count = max(result, max_count)
    print(max_count)




solution()