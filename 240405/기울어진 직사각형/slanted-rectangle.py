from math import sqrt

def solution():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]


    def in_range(x,y):
        return 0 <= x < n and 0 <= y < n

    def get_square_sum(i,j,k,l):
        sum_result = 0
        dxs, dys = [1, -1, -1, 1], [1, 1, -1, -1]
        move_nums = [k,l,k,l] # 주목 -> 내가 다루지 못해서 틀린 부분.
        
        current_x = i
        current_y = j

        for dx,dy,move_num in zip(dxs, dys, move_nums): # 이것도 주목. 이렇게 하면 가로, 세로 길이 똑같이 유지해서 직사각형 만들 수 있음.
        # 근데 사실 초반에 생각했던 접근 방법이 이것과 유사. 나도 가로 길이 + 세로 길이 나눠서 생각해야한다고 생각했었음.
        # 이 접근 방법에서 또한 굳이 zip을 쓸필요도 없음. 그냥 인덱스로 조정해서 move_nums에서 move_num을 선택하면 되지 않을까..
            for _ in range(move_num):
                # 시작점을 더하지 않아도 되는 이유: 마지막 4번째 탐색 때 더할 것이기 때문.
                current_x += dx
                current_y += dy

                if not in_range(current_x, current_y):
                    return 0
                sum_result += grid[current_x][current_y]
            
        return sum_result



    # < 흐름 >
    # n * n 격자의 각 모든 점(i,j)들을 탐색함.
    # 각 점들로부터 dx,dy 탐색을 이용
    # 스텝을 어디까지 늘릴 것인가? 직시각형에서 가장 길이가 긴 선분은 대각선: 대각선의 길이 만큼? 루트(n^2 + n^2)
    # 단, 격자 바깥을 빠져나가는지 안빠져나가는지 매번 확인해야함.

    # < 고려할 점 >
    # 한 지점으로부터 시작해서 반 시계 방향(정해진 방향이 있음)으로 순회
    # 각 방향으로 최소 1번은 움직여야 함. 즉, 1번 이상 움직일수도 있음.
    # 그런데 직사각형이 되어야함 -> 마주보는 변은 같은 길이여야
    # 그러면 그냥 가로, 세로 길이를 기록해놓자. 얼마만큼 최대로 갔는지. -> 가 아니라, 위의 get_square_sum 코드 참고하라. 어떻게 가로,세로 다루었는지.
    max_sum = 0
    for i in range(n):
        for j in range(n):
            # 몇 번 움직일것이냐...
            for k in range(1, int(sqrt(n ** 2 + n ** 2)) + 1):
                for l in range(1, int(sqrt(n ** 2 + n ** 2)) + 1): # 여기도 주목.
                    sum_result = get_square_sum(i,j,k,l)
                    max_sum = max(max_sum, sum_result)
    print(max_sum)

solution()