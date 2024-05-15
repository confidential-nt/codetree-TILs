# 큰 동전부터 거슬러주는 것이 항상 좋습니다. 그 이유는 주어진 동전들이 전부 배수관계에 놓여있기 때문

def solution():
    n,k = map(int, input().split())
    money = [int(input()) for _ in range(n)]
    count = 0
    for i in range(n-1, -1, -1):
        count += k // money[i]
        k %= money[i]
    print(count)    


solution()