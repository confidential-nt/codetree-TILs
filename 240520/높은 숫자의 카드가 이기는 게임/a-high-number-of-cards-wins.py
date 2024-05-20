def solution():
    n = int(input())
    a = []
    b = [int(input()) for _ in range(n)]
    b_set = set(b)
    for i in range(1, 2 * n + 1):
        if i not in b_set:
            a.append(i)

    a.sort()
    b.sort()
    
    count = 0
    b_index = 0
    for a_index in range(n):
        if b_index < n and a[a_index] > b[b_index]:
            count += 1
            b_index += 1
    print(count)


solution()