def solution():
    n,m = map(int, input().split())
    d1 = dict()
    d2 = dict()
    for i in range(1, n+1):
        string = input()
        d1[i] = string
        d2[string] = i
    
    for _ in range(m):
        q = input()
        if q.isalpha():
            print(d2[q])
        else:
            print(d1[int(q)])


solution()