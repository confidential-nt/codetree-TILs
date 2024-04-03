# 흐름
# 격자 바깥을 빠져나갈 수 있음. -> 중심점 (i,j) 단위로 K를 0부터 늘려나가면서
# 각 단계에서 금이 몇 개 있는지 파악 -> 금 가격과 K 격자의 비용 비교
# 손해라면 끝내기 -> 최대 금 개수 저장 (이미 손해라면 K를 증가시켜서 금 하나를 더 얻을 수 있어도 이미 손해이지 않을까 싶은 생각인데..아닌 것 같음. 그냥 다 해봐야할듯.) 
# 손해가 아니라면 K를 증가시킴

# 고려사항
# K를 어떻게 구현할 것이냐? 0일때는 특별 경우로 취급.((i,j)에 있는 값만 파악) 
# 1일 때부터 상하좌우 dx,dy?

def solution():
    n,m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    def get_num_of_gold(row,col,k):
        return sum([
            grid[i][j]
            for i in range(n)
            for j in range(n)
            if abs(row - i) + abs(col - j) <= k
        ])

    def get_area(k):
        return k * k + (k + 1) * (k + 1)

    max_gold = 0
    for i in range(n):
        for j in range(m):
            for k in range(2 * (n - 1) + 1):
                num_of_gold = get_num_of_gold(i,j,k)

                if num_of_gold * m >= get_area(k):
                    max_gold = max(max_gold, num_of_gold)
    print(max_gold)

solution()