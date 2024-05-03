def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    max_count = 0

    for h in range(1, 1001):
        count = 0

        if arr[0] > h :
            count += 1

        for i in range(1, n):
            if arr[i - 1] <= h and arr[i] > h:
                count += 1
        max_count = max(count, max_count)        
    print(max_count)
solution()