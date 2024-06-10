def solution():
    arr = list(map(int, input().split()))
    
    # 1. 이미 연속한 경우
    # 2. (각각 거리를 한칸씩 좁혀가면서 이동하는 방식으로 최대 이동횟수 만들기)
    # 2 - 1. 1이 아니면서, 왼쪽 끝 사람이 가장 먼저 이동하는 경우
    # 2 - 2. 1이 아니면서, 오른쪽 끝 사람이 가장 먼저 이동하는 경우
    # 최대로 만들어야하기 때문에 2씩 차이 나나 안나나 분석하는 것은 의미 없음.

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        print(0)
    
    else:
        max_move = 0
        move = arr[2] - arr[1] - 1
        max_move = max(max_move, move)

        move = arr[1] - arr[0] - 1
        max_move = max(max_move, move)

        print(max_move)

solution()