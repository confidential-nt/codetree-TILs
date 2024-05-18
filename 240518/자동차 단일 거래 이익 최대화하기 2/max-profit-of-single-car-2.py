def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = 0

    min_index = 0
    for i in range(1, n):
        if arr[min_index] > arr[i]:
            min_index = i
    
    for i in range(min_index, n):
        for j in range(i + 1, n):
            val = arr[j] - arr[i]
            max_val = max(val, max_val)
    
    if max_val <= 0:
        print(0)
    else:
        print(max_val)
            

   

    

solution()