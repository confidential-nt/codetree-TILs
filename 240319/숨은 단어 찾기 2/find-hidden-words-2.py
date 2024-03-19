def solution():
    N,M = map(int, input().split())
    arr = [[el for el in input()] for _ in range(N)]
    directions  = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != "L":
                continue
            
            e_count = 0
            current_x = i
            current_y = j
            for dx, dy in directions:
                while True:
                    nx = current_x + dx
                    ny = current_y + dy
                    if not (0 <= nx < N and 0 <= ny < M):
                        break
                    if arr[nx][ny] != "E":
                        break
                    e_count += 1
                    current_x = nx
                    current_y = ny
                    if e_count == 2:
                        count += 1
                        break
    print(count + 1)


solution()