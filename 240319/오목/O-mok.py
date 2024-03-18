from collections import deque

def solution():
    board = [
        list(map(int, input().split())) for _ in range(19)
    ]
    visited = [[False] * 19 for _ in range(19)]
    one_win = False
    one_trail = []
    two_win = False
    two_trail = []
    
    def bfs(start, num):
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        queue.append(start)
        visited[start[0]][start[1]] = True
        count = 1
        trail = [start]
        while queue:
            qx,qy = queue.popleft()

            for dx,dy in directions:
                nx,ny = qx + dx, qy + dy

                if not visited[nx][ny] and board[nx][ny] == num:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    trail.append((nx,ny))
                    count += 1
                    
        if count == 5:
            return [trail, count]
        else:
            return [[],count]
    # 1 탐색
    for i in range(19):
        for j in range(19):
            if not visited[i][j] and board[i][j] == 1:
                trail, count = bfs((i,j),1)
                if count == 5:
                    one_win = True
                    one_trail = trail
    # 2 탐색
    for i in range(19):
        for j in range(19):
            if not visited[i][j] and board[i][j] == 2:
                trail, count = bfs((i,j),2)
                if count == 5:
                    two_win = True
                    two_trail = trail

    if two_win:
        print("2")
        print(*[el + 1 for el in two_trail[2]])
    elif one_win:
        print("1")
        print(*[el + 1 for el in one_trail[2]])    
    else:
        print("0")




solution()