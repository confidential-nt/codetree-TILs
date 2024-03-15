def solution():
    n = int(input())
    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    min_distance = float("inf")
    for i in range(1, n - 1):
        dist = 0
        prev_index = 0
        # 굳이 또 배열을 생성하지 않고도 더할 수 있다.
        for j in range(1, n):
            if j == i :
                continue
            dist += abs(arr[prev_index][0] - arr[j][0]) + abs(arr[prev_index][1] - arr[j][1])
            prev_index = j
        min_distance = min(min_distance, dist)
    print(min_distance)
solution()