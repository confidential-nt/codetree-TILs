def solution():
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = 0
    # 시작 위치 결정
    for i in range(n):
        val = 0
        count = m
        index = i
        while count > 0:
            temp = arr[index]
            val += arr[index]
            index = temp - 1    
            count -= 1
        max_val = max(val, max_val)
        
        
    print(max_val)
solution()