def solution():
    x,y = map(int, input().split())
    count = 0
    for num in range(x, y + 1):
        if str(num) == str(num)[::-1]:
            count += 1
    print(count)    
    
    
solution()