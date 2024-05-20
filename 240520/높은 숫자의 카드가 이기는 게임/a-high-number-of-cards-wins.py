def solution():
    n = int(input())
    a = []
    b = [int(input()) for _ in range(n)]

    for i in range(1, 2 * n + 1):
        if i not in b:
            a.append(i)
    
    max_a = max(a)
    count = 0
    for i in range(n):
        if b[i] < max_a :
            count += 1
    print(count)






solution()