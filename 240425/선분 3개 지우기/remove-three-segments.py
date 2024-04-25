def solution():
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # 제외 시켜야할 선분. i,j,k
                # 겹치는가 안겹치는가를 어떻게 확인?
                count = [0] * (101)
                for l in range(n):
                    if l in [i,j,k]:
                        continue
                    x1,x2 = lines[l]
                    for c in range(x1,x2 + 1):
                        count[c] += 1           
                is_possible = True
                for index in range(0,101):
                    if count[index] > 1: # 경계든 그냥 겹치는 부분이든 해당 지점이 1이상 카운트되면 무조건 겹치거나 경계인 부분.
                        is_possible = False
                        break

                if is_possible:
                    answer += 1 
    print(answer)
solution()