def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    max_count = 0

    for h in range(1, 1001):
        temp = [el - h for el in arr]
        
        count = 0
        i = 0
        j = 1
        while i < n :
            if temp[i] <= 0:
                i += 1
                continue
            while j < n :
                if temp[j] <= 0:
                    count += 1
                    
                    j = i + 1 
                    break 
                j += 1       
              
            i = j + 1
        max_count = max(count, max_count)
    
    print(max_count)
solution()