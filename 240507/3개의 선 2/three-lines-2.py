from itertools import combinations

def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0

    # 가로 x 세로의 조합 (3가지 선택)
    # 각 조합에서 0~10까지 탐색.
    for i in range(4): # 가로(y) 0 ~ 3개
        j = 3 - i # 세로(x) 3 ~ 0 개

        possible = list(range(11))
        x = list(combinations(possible, j)) # 0~10 중 j개 선택한 x축 x[i]는 j개 선택한 경우의 수 중 하나. ex: j = 3인 경우 x[i]는 (1,2,3)
        y = list(combinations(possible, i)) # 0~10 중 i개 선택한 y축

        is_possible = [0] * n
        for cx in x:                    
            for index, (ax,ay) in enumerate(arr):
                if ax in cx:
                    is_possible[index] = 1

            for cy in y:
                for index, (ax,ay) in enumerate(arr):
                    if ay in cy:
                        is_possible[index] = 1
                if len([el for el in is_possible if el == 1]) == n :
                    answer = 1
                else:
                    is_possible = [0] * n
    print(answer)


solution()