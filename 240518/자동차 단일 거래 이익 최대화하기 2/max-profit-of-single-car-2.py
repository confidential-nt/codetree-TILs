def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    for i in range(n):
        for j in range(i+1, n):
            val = arr[j] - arr[i]
            max_val = max(val, max_val)
    
    if max_val < 0:
        print(0)
    else:
        print(max_val)

    

solution()