def solution():
    a,b,c = map(int, input().split())
    max_val = 0
    for i in range(c):
        for j in range(c):
            if a * i + b * j <= c:
                max_val = max(a * i + b * j, max_val)
    print(max_val)

solution()