import sys

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    max_sum_res = -sys.maxsize
    sum_res = 0
    
    for i in range(n):
        if sum_res < 0: 
            sum_res = arr[i]
        else:
            sum_res += arr[i]
        max_sum_res = max(max_sum_res, sum_res)
        
        
    print(max_sum_res)       


solution()