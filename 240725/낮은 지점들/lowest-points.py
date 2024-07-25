def solution():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    
    d = dict()
    for x,y in coords:
        if x not in d:
            d[x] = []
        d[x].append(y)
    
    for key,value in d.items():
        d[key] = sorted(value)
    
    for key,value in d.items():
        d[key] = value[0]
    print(sum(d.values()))

solution()