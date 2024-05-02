def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    max_count = 0
    for k in range(1, max(arr)):
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] - k == k - arr[j]:
                    count += 1
        max_count = max(count, max_count)
    print(max_count)            

solution()