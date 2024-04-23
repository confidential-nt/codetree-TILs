from itertools import combinations

def solution():
    K,N = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(K)]
    temp = []
    count = len(list(combinations(scores[0], 2)))
    for score in scores:
        combs = list(combinations(score, 2))
        if len(temp) == 0:
            temp = combs
            continue
        for comb in combs:
            if comb not in temp:
                count -= 1
    print(count)




solution()