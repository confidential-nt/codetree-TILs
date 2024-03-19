import sys

def solution():
    board = [list(map(int, input().split())) for _ in range(19)]
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            
            for dx,dy in directions: # 한 방향에 대해서
                count = 1
                current_x = i
                current_y = j
                while True: # 이렇게 상,하,좌,우,대각선 방향으로 어떻게 탐색할 것인지 생각을 못했음.
                    # 입력이 이렇게 작은 상황에서는 무한 루프 돌아도 ㅇㅋ.
                    nx = current_x + dx
                    ny = current_y + dy
                    if not (0 <= nx < 19 and 0<= ny < 19):
                        break
                    if board[nx][ny] != board[i][j]:
                        break
                    count += 1
                    current_x = nx
                    current_y = ny

                    if count == 5:
                        print(board[i][j])
                        print(i + 2 * dx + 1, j + 2 * dy + 1)
                        sys.exit()
    print(0)

solution()