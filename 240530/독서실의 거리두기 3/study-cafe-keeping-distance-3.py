# 현재 상황에서 최선의 선택이 무엇일지를 일일이 따져보며, 최선의 상황으로 가는 전략을 최대한 단순화하는 연습을 많이 해봐야합니다. 컴퓨터를 이용하여 문제 해결을 하는 것이기 때문에, 수학적 규칙을 찾아 해결하기 보다는 되도록 컴퓨터에게 일을 위임하여 해결할 수 있는 전략을 생각해보는 것을 습관화 하는 것이 중요합니다.

# Step 0. 초기 위치
# 1 0 1 0 1 0 0 0 0 0 1

# Step 1. 가장 먼 1 간의 쌍 찾기 (Y로 표기)
# 1 0 1 0 Y 0 0 0 0 0 Y
# 만약 가장 멀리 있는 쌍이 2개 이상인 경우라면? 둘 중 하나를 선택하면 어차피 다른 곳은 그대로 가장 멀리있는 쌍임.
# 따라서 사람 한 명을 추가하여 가장 멀리 떨어져 있는 간격을 처음보다 더 줄일 수 없음.

# Step 2. 해당 쌍 가운데에 1 놓기
# 1 0 1 0 1 0 0 1 0 0 1

# Step 3. 다시 가장 먼 1간의 쌍 찾기 (Z로 표기)
# 1 0 1 0 Z 0 0 Z 0 0 1

# Step 4. Z간의 간격이 답 → 3

# 문제 해석 유의
def solution():
    # 한 명을 더 집어넣었을 때 가장 가까운 두 사람 간의 거리를 최대로 한다.
    # 가장 가까운 쌍에 대해서 찾으면 그 사이에 한 명을 더 집어넣었을 때 두 사람 간의 거리를 최대로 한다는 것은 어불성설.
    # 그래야 가장 가까이에 있는 사람간의 거리에 영향을 최대한 덜 주게 됨.
    # 가장 최대로 하는 법: 가장 먼 쌍을 찾는다 -> 그 가운데에 누군가를 집어넣는다 -> 그리고나서 가장 가까운 두 사람의 거리를 찾는다.
    # 거리두기 -> 최소 한 칸은 떨어져있어야한다는건가? -> x
    n = int(input())
    arr = [int(el) for el in input()]

    # 1. 가장 먼 쌍 찾기
    max_distance = -1
    max_distance_pair = (0,0)
    for i in range(n):
        if arr[i] == 0:
            continue
        for j in range(i+1, n):
            if arr[j] == 0:
                continue      
            distance = j - i
            if distance > max_distance:
                max_distance = distance
                max_distance_pair = (i,j)
            break
    
    # 2. 해당 쌍 가운데에 1 놓기
    pos = (max_distance_pair[0] + max_distance_pair[1]) // 2
    arr[pos] = 1
    
    # 3. 최솟값 구하기
    result_distane = float("inf")
    for i in range(n):
        if arr[i] == 0:
            continue
        for j in range(i+1, n):
            if arr[j] == 0:
                continue      
            distance = j - i
            result_distane = min(distance, result_distane)
            break
    print(result_distane)






    
    

solution()