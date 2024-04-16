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
            if (x3< x1 <x4 and x3 < x2 < x4) or (x1 < x3 < x2 and x1 < x4 < x2) or (x4< x1 <x3 and x4 < x2 < x3) or (x2 < x3 < x1 and x2 < x4 < x1):
                count += 1
    result = n - count
    print(result if result > 0 else 0)    


solution()