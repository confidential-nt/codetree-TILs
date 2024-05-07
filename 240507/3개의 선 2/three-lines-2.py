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
        y = list(combinations(possible, i))
        x = list(combinations(possible, j))

        
        for index, (ax,ay) in enumerate(arr):
            temp = [0]* n
            for cx in x:
                for cy in y:
                    if ax in cx:
                        temp[index] = 1
                    if ay in cy:
                        temp[index] = 1   

            if len([el for el in temp if el == 1]) == n:
                answer = 1
                break

        if answer == 1:
            break

    print(answer)


solution()