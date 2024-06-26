import sys

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    # 양의 정수 3개
    case_1 = 1
    arr_copy = sorted(arr)
    count = 0
    for i in range(n-1, -1, -1):
        if count >= 3:
            break
        if arr_copy[i] > 0:
            case_1 *= arr_copy[i]
            count += 1

    # 양 2, 음 1
    case_2 = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count_plus = 0
    count_minus = 0

    for i in range(n):
        if arr_copy[i] == 0:
            continue
        if count_plus < 2 and arr_copy[i] > 0:
            case_2 *= arr_copy[i]
            count_plus += 1
        elif count_minus < 1 and arr_copy[i] < 0:
            case_2 *= arr_copy[i]
            count_minus += 1

    # 양1, 음2
    case_3 = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count_plus = 0
    count_minus = 0
    for i in range(n-1, -1, -1):
        if arr_copy[i] == 0:
            continue
        if count_plus < 1 and arr_copy[i] > 0:
            case_3 *= arr_copy[i]
            count_plus += 1
        elif count_minus < 2 and arr_copy[i] < 0:
            case_3 *= arr_copy[i]
            count_minus += 1

    # 음 3
    case_4 = 1
    arr_copy = sorted(arr, key=lambda x: abs(x))
    count = 0
    for i in range(n):
        if count >= 3:
            break
        if arr_copy[i] < 0:
            case_4 *= arr_copy[i]
            count += 1
    # 영 포함
    case_5 = -sys.maxsize
    for i in range(n):
        if arr[i] == 0:
            case_5 = 0
            
    print(max(case_1, case_2, case_3, case_4, case_5))
solution()