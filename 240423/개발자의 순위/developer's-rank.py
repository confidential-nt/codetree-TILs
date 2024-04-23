from itertools import combinations

def solution():
    K,N = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(K)]
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            comb = (i,j)

            is_immutable = True
            for score in scores:
                score_comb = list(combinations(score, 2))
                
                if comb not in score_comb:
                    is_immutable = False
                    break
            
            if is_immutable:
                count += 1

    print(count)




solution()