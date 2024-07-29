from itertools import combinations

def solution():
    n,m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    count = 0
    
    for x,y,z in combinations(range(m), 3):
        s = set()
        for i in range(n):
            a1 = a[i][x] + a[i][y] + a[i][z]
            s.add(a1)
        
        is_possible = True
        for i in range(n):
            b1 = b[i][x] + b[i][y] + b[i][z]
            if b1 in s:
                is_possible = False
                break
        
        if is_possible:
            count += 1
            
    print(count)

solution()