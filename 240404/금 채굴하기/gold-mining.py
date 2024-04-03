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
        if k == 0:
            return grid[row][col] # K = 0 일때

        
        curr_x, curr_y = row - k, col # 시작지점. k=1일때 시작지점은 중심점보다 row가 하나 위인 곳임.
        for dx,dy in zip(dxs, dys):
            for step in range(k):
                if in_range(curr_x, curr_y):
                    num_of_gold += grid[curr_x][curr_y]
                curr_x += dx
                curr_y += dy    
        return num_of_gold

    max_gold = 0
    for i in range(n):
        for j in range(n):
            num_of_gold = 0
            for k in range(2 * n + 1): # 2 * n 은 내가 생각했을 때 더 합리적이라 생각해서 판단한 범위임..
                num_of_gold += get_num_of_gold(i,j,k) # 매번 구하는게 아니라 한번씩만

                if num_of_gold * m >= get_area(k):
                    max_gold = max(max_gold, num_of_gold)
    print(max_gold)
solution()
# 내가 처음에 생각 한 것이 아예 틀리지는 않았음. 다만 각각의 가장 자리를 더할 생각 + 그 것을 더하기 위해 발견해야할 규칙을 발견하지 못함.