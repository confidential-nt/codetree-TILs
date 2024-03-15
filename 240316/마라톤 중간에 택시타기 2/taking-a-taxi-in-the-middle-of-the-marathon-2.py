def solution():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    
    min_distance = float("inf")
    for i in range(1, N - 1):
        temp = arr[i]
        arr[i] = (0,0)
        distance = get_distance(arr, N)
        min_distance = min(distance, min_distance)
        arr[i] = temp
    print(min_distance)

def get_distance(arr, N):
    result = 0
    for i in range(2, N + 1):
        # for j in range(i-2, i):
        result += (abs(arr[i - 2][0] - arr[i - 1][0]) + abs(arr[i - 2][1] - arr[i - 1][1]))
    return result


solution()