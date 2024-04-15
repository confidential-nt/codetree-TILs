def solution():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    min_distance = float("inf")

    for i in range(n):
        for j in range(i+1, n):
            x1,y1 = coords[i]
            x2,y2 = coords[j]
            result = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            min_distance = min(min_distance, result)
    print(min_distance)

solution()