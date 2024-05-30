# 이처럼 최선의 답을 구하는 문제에서는, 여러 다양한 상황을 가정해보며 고려해야 할 모든 가짓수를 나열한 뒤, 그 중 가장 좋은 답을 선택하는 식으로 문제를 해결할 수 있습니다.

def solution():
    a,b,x,y = map(int, input().split())

    # 3 10 8 2
    # x -> y or y -> x

    # 1. x -> y
    case1 = abs((x - a)) + abs((y - b))


    # 2. y -> x
    case2 = abs((y - a)) + abs((x - b))

    # 3. a -> b
    print(min(abs(a - b), case1, case2))

solution()