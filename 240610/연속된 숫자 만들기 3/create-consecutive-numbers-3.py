def solution():
    arr = list(map(int, input().split()))

    # 1. 이미 정렬 되었을 때 1 2 3
    # 2. 한 곳만 원하는대로 정렬 되었을 때 1 4 6 -> 1 3 4 -> 1 2 3
    # 3. 다 정렬 안되었을 때 8 20 21 -> 8 19 20 -> 8 18 19 -> 8 17 18 

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        print(0)
    
    elif arr[0] + 2 == arr[1] or arr[1] + 2 == arr[2]:
        print(2)

    else:
        print(arr[1] - arr[0] - 1)

solution()