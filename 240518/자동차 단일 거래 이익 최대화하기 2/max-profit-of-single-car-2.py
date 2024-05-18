def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = 0

    min_index = 0
    for i in range(1, n):
        if arr[min_index] > arr[i]:
            min_index = i
    
    max_index = min_index
    for i in range(min_index + 1, n):
        if arr[max_index] < arr[i]:
            max_index = i
    
    val = arr[max_index] - arr[min_index]

    if val <= 0:
        print(0)
    else:
        print(val)
            

   

    

solution()