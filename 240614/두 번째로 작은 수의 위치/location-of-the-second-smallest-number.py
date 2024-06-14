# 두번째로 작은 수 === 가장 작은 수가 있고 그 다음으로 작다.

def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    min_num = min(arr)
    value = float("inf")
    answer = -1
    for i in range(n):
        if arr[i] == min_num:
            continue
        if arr[i] == value:
            answer = -1
            continue
        if arr[i] < value:
            value = arr[i]
            answer = i + 1
    print(answer)    
solution()