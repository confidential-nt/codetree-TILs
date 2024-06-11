# 앞선 문제와 다른 점은 무조건 양 쪽 끝에 사람이 앉지는 않는다는 것.

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
    
    arr[pos] = 0
    
    if arr[0] == 0:
        other_distance = float("inf")
        arr[0] = 1
        for i in range(n):
            if arr[i] == 0:
                continue
            for j in range(i+1, n):
                if arr[j] == 0:
                    continue      
                distance = j - i
                other_distance = min(distance, other_distance)
                break
        if other_distance > result_distane:
            result_distane = other_distance        
        arr[0] = 0
        
    if arr[n - 1] == 0:
        other_distance = float("inf")
        arr[n - 1] = 1
        for i in range(n):
            if arr[i] == 0:
                continue
            for j in range(i+1, n):
                if arr[j] == 0:
                    continue      
                distance = j - i
                other_distance = min(distance, other_distance)
                break
        if other_distance > result_distane:
            result_distane = other_distance
        
    print(result_distane)






    
    

solution()