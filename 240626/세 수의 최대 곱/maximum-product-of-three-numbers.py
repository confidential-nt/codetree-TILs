import sys


def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    # 양의 정수 3개
    case_one = -sys.maxsize
    for i in range(n):
        if arr[i] <= 0:
            continue
        for j in range(i+1, n):
            if arr[j] <= 0:
                continue
            for k in range(j+1, n):
                if arr[k] <= 0:
                    continue
                case_one = max(arr[i] * arr[j] * arr[k], case_one)

    # 양 2, 음 1
    case_two = -sys.maxsize
    for i in range(n):
        if arr[i] <= 0:
            continue
        for j in range(i+1, n):
            if arr[j] <= 0:
                continue
            for k in range(n):
                if arr[k] < 0:
                    case_two = max(arr[i] * arr[j] * arr[k], case_two)
    # 양1, 음2
    case_three = -sys.maxsize
    for i in range(n):
        if arr[i] <= 0:
            continue
        for j in range(n):
            if arr[j] > 0:
                continue
            for k in range(j+1, n):
                if arr[k] > 0:
                    continue
                case_three = max(arr[i] * arr[j] * arr[k], case_three)
    # 음 3
    case_four = -sys.maxsize
    for i in range(n):
        if arr[i] > 0:
            continue
        for j in range(i+1, n):
            if arr[j] > 0:
                continue
            for k in range(j+1, n):
                if arr[k] > 0:
                    continue
                case_four = max(arr[i] * arr[j] * arr[k], case_four)
    # 영 포함
    case_five = -sys.maxsize
    for i in range(n):
        if arr[i] == 0:
            case_five = 0

    print(max([case_one, case_two, case_three, case_four, case_five]))
solution()