def solution():
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    s2 = list(map(int, input().split()))

    for s in s2:
        if s in s1:
            print(1, end=" ")
        else:
            print(0, end=" ")

solution()