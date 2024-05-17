def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    
    arr.sort(key=lambda x: x[1])
    last = -1
    count = 0
    for (s,e) in arr:
        if last <= s:
            count += 1
            last = e
    print(count)        

solution()