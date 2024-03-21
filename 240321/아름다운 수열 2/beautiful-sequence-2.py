def solution():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in range(N - M + 1):
        piece = A[i:i+M]
        if sorted(piece) == sorted(B):
            count += 1

    print(count)



solution()