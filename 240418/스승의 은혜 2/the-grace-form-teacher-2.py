def solution():
    N,B = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(int(input()))
    
    max_count = 0
    for i in range(N):
        count = 0
        total = 0
        for j in range(N):
            if i == j:
                if total + (P[j] // 2) <= B:
                    total += (P[j] // 2)
                    count += 1
                continue
            if total + (P[j]) <= B:
                    total += (P[j])
                    count += 1
        max_count = max(max_count, count)    
    print(max_count)

solution()