# 나는 bfs로 풀었는데 더 간단한 방법이 있음.
# L,R,B의 위치를 기록한다음, L과 B가 가로 또는 세로 방향으로 일직선상에 있는 경우와 일직선상에 존재하지 않는 경우로
# 나누어 생각해보면 됨.
# -> 최단 경로를 구하는 것임: 돌아갈 필요 없이 바로 L에서 B로 최대한 가야 최단 경로를 구할 수 있음
# -> 이렇게 생각해보면, 주어지는 입력의 모양까지 고려했을 때 갈수 있는 경로의 모양이 한정되어짐.

# 이러한 n x n 배열의 최단 거리: abs(x1 - x2) + abs(y1 - y2)

# 다음과 같은 3가지 케이스를 고려

# 1. L과 B가 일직선상에 없는 경우
# : 반드시 L에서 B로 가는 최단 경로 중에 R을 피해서 갈 수 있는 경로가 존재 -> 최단 경로 바로 구하면 됨.

# 2. L과 B가 세로 방향으로 일직선상에 존재하는 경우
# : L에서 B로 가는 최단 경로 중에 R이 존재한다면 2칸만 돌아가면 됨. 존제하지 않는다면 일직선으로 가면 됨.

# 3. L과 B가 가로 방향으로 일직선상에 존재하는 경우
# : 2와 비슷.

n = 10
board = [
    input()
    for _ in range(n)
]
    
# L, R, B의 위치를 찾습니다.
for i in range(n):
    for j in range(n):
        if board[i][j] == 'L':
            l_x = i
            l_y = j
        if board[i][j] == 'R':
            r_x = i
            r_y = j
        if board[i][j] == 'B':
            b_x = i
            b_y = j

# Case 1 : L과 B가 일직선상에 없다면, 반드시 L에서 B를 가는 최단경로중에
# R을 피해서 갈 수 있는 경로가 있습니다.
# 따라서 L과 B가 일직선상이 아니라면 L과 B의 최단경로를 구해주면 됩니다.
if l_x != b_x and l_y != b_y:
    # 최단 경로 구하는 법.
    print(abs(l_x - b_x) + abs(l_y - b_y) - 1)

# Case 2 : L과 B가 세로 방향으로 일직선상에 있다면,
# 그 일직선 사이에 R이 있을 때에는 2칸 돌아갑니다.
# 그 외의 모든 경우에 대해 L과 B의 최단경로를 그대로 구해주면 됩니다.
elif l_y == b_y: # L과 B가 세로 방향으로 일직선상에 있는데
    # R도 세로 방향으로 일직선상에 있고 x좌표가 B,L 사이에 있는 경우에는 (즉, R이 정확히 L,B 사이에 있는 경우)
    if l_y == r_y and r_x >= min(b_x, l_x) and r_x <= max(b_x, l_x):
        # abs(l_x - b_x) + abs(l_y - b_y) - 1 + (2)
        print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
    else:
        print(abs(l_x - b_x) + abs(l_y - b_y) - 1)

# Case 3 : L과 B가 가로 방향으로 일직선상에 있다면,
# 그 일직선 사이에 R이 있을 때에는 2칸 돌아갑니다.
# 그 외의 모든 경우에 대해 L과 B의 최단경로를 그대로 구해주면 됩니다.
elif l_x == b_x:
    if l_x == r_x and r_y >= min(b_y, l_y) and r_y <= max(b_y, l_y):
        print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
    else:
        print(abs(l_x - b_x) + abs(l_y - b_y) - 1)