def solution():
    a,b,x,y = map(int, input().split())

    # 3 10 8 2
    # x -> y or y -> x

    # 1. x -> y
    case1 = abs((x - a)) + abs((y - b))


    # 2. y -> x
    case2 = abs((y - a)) + abs((x - b))

    print(min(case1, case2))

solution()