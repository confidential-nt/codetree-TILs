from itertools import permutations

def solution():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    all_permutations = set(permutations(B,M))
    
    count = 0
    for i in range(N):
        piece = A[i:i+M]
        if len(piece) != M:
            break
        for perm in all_permutations:
            if tuple(piece) == perm:
                count += 1
    print(count)



solution()