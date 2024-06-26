import sys

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    # 양의 정수 3개
    case_1 = -sys.maxsize
    result = 1
    arr_copy = sorted(arr)
    count = 0
    
    for i in range(n-1, -1, -1):
        if count >= 3:
            break
        if arr_copy[i] > 0:
            result *= arr_copy[i]
            count += 1
    case_1 = result if count >= 3 else -sys.maxsize


    # 양 2, 음 1
    case_2 = -sys.maxsize
    result = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count_plus = 0
    count_minus = 0
    
    for i in range(n):
        if arr_copy[i] == 0:
            continue
        if count_plus < 2 and arr_copy[i] > 0:
            result *= arr_copy[i]
            count_plus += 1
        elif count_minus < 1 and arr_copy[i] < 0:
            result *= arr_copy[i]
            count_minus += 1
    case_2 = result if count_minus + count_plus >= 3 else -sys.maxsize

    # 양1, 음2
    case_3 = -sys.maxsize
    result = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count_plus = 0
    count_minus = 0
    for i in range(n-1, -1, -1):
        if arr_copy[i] == 0:
            continue
        if count_plus < 1 and arr_copy[i] > 0:
            result *= arr_copy[i]
            count_plus += 1
        elif count_minus < 2 and arr_copy[i] < 0:
            result *= arr_copy[i]
            count_minus += 1
    case_3 = result if count_minus + count_plus >= 3 else -sys.maxsize

    # 음 3
    case_4 = -sys.maxsize
    result = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count = 0
    for i in range(n):
        if count >= 3:
            break
        if arr_copy[i] < 0:
            result *= arr_copy[i]
            count += 1
    case_4 = result if count >= 3 else -sys.maxsize

    # 영 포함
    case_5 = -sys.maxsize
    for i in range(n):
        if arr[i] == 0:
            case_5 = 0

    
    print(max(case_1, case_2, case_3, case_4, case_5))
solution()