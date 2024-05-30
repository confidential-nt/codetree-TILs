# 현재 상황에서 최선의 선택이 무엇일지를 일일이 따져보며, 최선의 상황으로 가는 전략을 최대한 단순화하는 연습을 많이 해봐야합니다. 컴퓨터를 이용하여 문제 해결을 하는 것이기 때문에, 수학적 규칙을 찾아 해결하기 보다는 되도록 컴퓨터에게 일을 위임하여 해결할 수 있는 전략을 생각해보는 것을 습관화 하는 것이 중요합니다.

# Step 0. 초기 위치
# 1 0 1 0 1 0 0 0 0 0 1

# Step 1. 가장 먼 1 간의 쌍 찾기 (Y로 표기)
# 1 0 1 0 Y 0 0 0 0 0 Y

# Step 2. 해당 쌍 가운데에 1 놓기
# 1 0 1 0 1 0 0 1 0 0 1

# Step 3. 다시 가장 먼 1간의 쌍 찾기 (Z로 표기)
# 1 0 1 0 Z 0 0 Z 0 0 1

# Step 4. Z간의 간격이 답 → 3

def solution():
    # 가장 가까운 두 사람 간의 거리를 최대로 한다. -> 가장 가까운 쌍을 골라 그 안에 사람을 앉혀야한다.
    # 거리두기 -> 최소 한 칸은 떨어져있어야한다는건가?
    n = int(input())
    arr = [int(el) for el in input()]

    # 1. 가장 가까운 쌍 찾기
    min_distance = float("inf")
    min_distance_pair = (0,0)
    for i in range(n):
        if arr[i] == 0:
            continue
        for j in range(i+1, n):
            if arr[j] == 0:
                continue      
            distance = j - i
            min_distance = min(distance, min_distance)
            min_distance_pair = (i,j)
    
    # 2. 해당 쌍 가운데에 1 놓기
    pos = (min_distance_pair[0] + min_distance_pair[1]) // 2
    arr[pos] = 1

    # 3. 최댓값 구하기
    result_distane = float("inf")
    for i in range(n):
        if arr[i] == 0:
            continue
        for j in range(i+1, n):
            if arr[j] == 0:
                continue      
            distance = j - i
            result_distane = min(distance, result_distane)
    print(result_distane)






    
    

solution()