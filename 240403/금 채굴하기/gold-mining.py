def solution():
    n,m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    def get_area(k):
        return k * k + (k + 1) * (k + 1)

    def in_range(x,y):
        return 0 <= x < n and 0 <= y < n

    def get_num_of_gold(row,col,k):
        num_of_gold = 0
        dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]
        num_of_gold += grid[row][col] # K = 0 일때

        for curr_k in range(1, k + 1):
            curr_x, curr_y = row - curr_k, col # 시작지점. k=1일때 시작지점은 중심점보다 row가 하나 위인 곳임.
            for dx,dy in zip(dxs, dys):
                for step in range(curr_k):
                    if in_range(curr_x, curr_y):
                        num_of_gold += grid[curr_x][curr_y]
                    curr_x += dx
                    curr_y += dy    
        return num_of_gold

    max_gold = 0
    for i in range(n):
        for j in range(n):
            for k in range(2 * n + 1):
                num_of_gold = get_num_of_gold(i,j,k)

                if num_of_gold * m >= get_area(k):
                    max_gold = max(max_gold, num_of_gold)
    print(max_gold)
solution()