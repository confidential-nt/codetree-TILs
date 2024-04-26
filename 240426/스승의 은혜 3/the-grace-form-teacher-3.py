def solution():
    N,B = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)] # (선물, 배송비)
    max_count = 0
    for i in range(N):
        tmp = [el for el in arr]
        tmp[i] = (tmp[i][0]/2, tmp[i][1])
        
        tmp.sort(key=lambda x:x[0]+x[1])

        count = 0
        total = 0

        for j in range(N):
            if total + tmp[j][0] + tmp[j][1] <= B:
                total += tmp[j][0] + tmp[j][1]
                count += 1
        max_count = max(count, max_count)

    print(max_count)    


solution()