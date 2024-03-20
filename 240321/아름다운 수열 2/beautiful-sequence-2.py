from itertools import permutations

def solution():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    all_combinations = set(list(permutations(B, len(B))))
    
    count = 0
    for i in range(N):
        for j in range(i, N):
            piece = A[i:j+1]
            for comb in all_combinations:
                if comb == tuple(piece):
                    count += 1
    print(count)



solution()