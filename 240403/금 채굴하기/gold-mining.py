def solution():
    n,m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    def get_num_of_gold(row,col,k):
        return sum([
            grid[i][j]
            for i in range(n)
            for j in range(n)
            if abs(row - i) + abs(col - j) <= k
            # 굳이 마름모를 직접 그리는 것을 가정하지 않아도 간접적으로 도출할 수 있음.
            # 어떻게? 모든 격자의 각 칸에 대하여, 이처럼 거리를 계산하여 k라는 거리 안에 들어오는가를 계산해서.
        ])

    def get_area(k):
        return k * k + (k + 1) * (k + 1)

    max_gold = 0
    for i in range(n):
        for j in range(n):
            for k in range(2 * (n - 1) + 1): # 나는 손해가 나는 즉시 계산을 중단해도 괜찮다고 생각했는데 더 안전빵으로 그냥 nxn격자를 다 채울 범위까지 반복하는 게 나은듯.
            # 다만 k를 어디까지 늘릴거냐는 정하기 나름인듯. 물론 어쨌든 격자를 다 채워야하긴 하는 것 같다만..
            # 이런식으로 재량껏 범위를 한정하는 능력이 중요한듯.
                num_of_gold = get_num_of_gold(i,j,k)

                if num_of_gold * m >= get_area(k):
                    max_gold = max(max_gold, num_of_gold)
    print(max_gold)

solution()