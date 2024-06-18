from collections import deque

def solution():
    n = 10
    arr = [[el for el in input()] for _ in range(n)]
    answer = float("inf")
    def bfs(x,y):
        nonlocal answer
        queue = deque([(x,y,0)])
        visited = [([False] * n) for _ in range(n)] 
        visited[x][y] = True
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            qx,qy,distance = queue.popleft()
            if arr[qx][qy] == "B":
                answer = min(answer, distance)
                continue

            for dx,dy in directions:
                nx = qx + dx
                ny = qy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] != "R":
                    queue.append((nx,ny,distance + 1))
                    visited[nx][ny] = True
    
    start = (0,0)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "L":
                start = (i,j)
                break

    bfs(start[0],start[1])
    print(answer - 1)

solution()