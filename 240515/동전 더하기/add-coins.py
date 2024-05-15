def solution():
    n,k = map(int, input().split())
    money = [int(input()) for _ in range(n)]
    count = 0
    for i in range(n-1, -1, -1):
        count += k // money[i]
        k %= money[i]
    print(count)    


solution()