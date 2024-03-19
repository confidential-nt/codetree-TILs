from collections import defaultdict

def solution():
    N,K = map(int, input().split())
    R = 10000 # 위치의 범위가 10000으로 고정되어있다는 점에 유의. -> 10000인 위치까지 봐야한다.
    placed = [0] * (R + 1)

    for _ in range(N):
        loc, alpha = input().split()
        loc = int(loc)
        placed[loc] = 2 if alpha == "H" else 1
    
    max_score = 0
    for i in range(1, R - K + 1):
        score = 0
        for j in range(i, i+K+1):
            score += placed[j]
        max_score = max(max_score, score)
    print(max_score)


solution()