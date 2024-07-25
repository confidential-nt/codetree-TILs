def solution():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    
    d = dict()
    for x,y in coords:
        if x not in d:
            d[x] = []
        d[x].append(y)
    
    for key,value in d.items():
        d[key] = sorted(value)
    
    for key,value in d.items():
        d[key] = value[0]
    print(sum(d.values()))

def solution2():
    # 변수 선언 및 입력:
    n = int(input())
    min_y = {}

    # 각 x마다 최소 y만 저장해줍니다.
    for _ in range(n):
        x, y = tuple(map(int, input().split()))

        # 아직 map에 해당 x가 없다면 y값을 그대로 넣어줍니다.
        if x not in min_y:
            min_y[x] = y
        # 그렇지 않다면, 최소 y를 넣어줍니다.
        else:
            min_y[x] = min(min_y[x], y)

    # 답을 저장합니다.
    sum_val = 0

    # map에 들어있는 값들을 순회합니다.
    for value in min_y.values():
        # value에 해당하는 y값을 더해줍니다.
        sum_val += value

    print(sum_val)

solution()