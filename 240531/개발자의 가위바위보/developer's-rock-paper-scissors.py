def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    max_count = 0
    # 1. 1 -> 가위 / 2 -> 바위 / 3 -> 보
    count1 = 0 # 첫번째 개발자가 이기는 횟수
    for (i,j) in arr:
        if i == 1 and j == 3:
            count1 += 1
        elif i == 2 and j == 1:
            count1 += 1
        elif i == 3 and j == 2:
            count1 += 1
    max_count = max(count1, max_count)

    # 2. 1 -> 바위 / 2 -> 가위 / 3 -> 보
    count2 = 0
    for (i,j) in arr:
        if i == 1 and j == 2:
            count2 += 1
        elif i == 2 and j == 3:
            count2 += 1
        elif i == 3 and j == 1:
            count2 += 1
    max_count = max(count2, max_count)
    # 3. 1 -> 가위 / 2 -> 보 / 3 -> 바위
    count3 = 0
    for (i,j) in arr:
        if i == 1 and j == 2:
            count3 += 1
        elif i == 2 and j == 3:
            count3 += 1
        elif i == 3 and j == 1:
            count3 += 1
    max_count = max(count3, max_count)
    # 4. 1 -> 보 / 2 -> 가위 / 3 -> 바위
    count4 = 0
    for (i,j) in arr:
        if i == 1 and j == 3:
            count4 += 1
        elif i == 2 and j == 1:
            count4 += 1
        elif i == 3 and j == 2:
            count4 += 1
    max_count = max(count4, max_count)
    # 5. 1 -> 보 / 2 -> 바위 / 3 -> 가위
    count5 = 0
    for (i,j) in arr:
        if i == 1 and j == 2:
            count5 += 1
        elif i == 2 and j == 3:
            count5 += 1
        elif i == 3 and j == 1:
            count5 += 1
    max_count = max(count5, max_count)
    # 6. 1 -> 바위 / 2 -> 보 / 3 -> 가위
    count6 = 0
    for (i,j) in arr:
        if i == 1 and j == 3:
            count6 += 1
        elif i == 2 and j == 1:
            count6 += 1
        elif i == 3 and j == 2:
            count6 += 1
    max_count = max(count6, max_count)
    print(max_count)
solution()