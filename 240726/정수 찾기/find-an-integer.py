def solution():
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    arr = list(map(int, input().split()))

    for el in arr:
        if el in s1:
            print(1)
        else:
            print(0)

solution()