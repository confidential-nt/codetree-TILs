def solution():
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1,x2 = lines[i] # base
            x3,x4 = lines[j] # 비교대상
            
            if (x1 > x3 and x2 < x4) or (x1 < x3 and x2 > x4):
                count += 1
            
    result = n - count
    print(result if result > 0 else 0) # 겹치는 횟수가 아니라 겹치는 선분의 수.    


solution()