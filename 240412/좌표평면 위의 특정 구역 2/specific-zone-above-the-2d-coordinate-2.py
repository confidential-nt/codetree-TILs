def solution():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    answer = float("inf")
    for i in range(n):
        max_x = -1
        max_y = -1
        min_x = float("inf")
        min_y = float("inf")
        for j in range(n):
            if i == j:
                continue
            max_x = max(max_x, coords[j][0])
            min_x = min(min_x, coords[j][0])
            max_y = max(max_y, coords[j][1])
            min_y = min(min_y, coords[j][1])
        area = (max_x - min_x) * (max_y - min_y)        
        answer = min(area, answer)
    print(answer)
            

solution()