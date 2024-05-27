def solution():
    n = int(input())
    times = [tuple(map(int, input().split())) for _ in range(n)]
    times.sort(key=lambda x:x[1])

    last = -1
    count = 0
    for (s,e) in times:
        if s >= last:
            count += 1
            last = e

    print(n - count)


        


solution()