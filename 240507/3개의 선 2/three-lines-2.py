from itertools import combinations

def solution():
    # 가장 노가다인게 가장 정확한 방법.
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0

    # 가로 x 세로의 조합 (3가지 선택)
    # 각 조합에서 0~10까지 탐색.
    for i in range(11):
        for j in range(11):
            for k in range(11):
                # x축 3개
                success = True
                for x,y in arr:
                    if x == i or x == j or x == k:
                        continue
                    success = False
                if success:
                    answer = 1
                
                # x 2, y 1
                success = True
                for x,y in arr :
                    if x == i or x == j or y == k:
                        continue
                    success = False
                
                if success:
                    answer = 1

                # x 1 y 2
                success = True
                for x,y in arr :
                    if x == i or y == j or y == k:
                        continue
                    success = False
                
                if success:
                    answer = 1

                # y 3
                success = True
                for x,y in arr :
                    if y == i or y == j or y == k:
                        continue
                    success = False
                
                if success:
                    answer = 1

                

    print(answer)


solution()