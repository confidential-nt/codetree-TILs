import heapq

def solution():
    n = int(input())
    bombs = [tuple(map(int, input().split())) for _ in range(n)]
    max_t = max([el[1] for el in bombs])

    def get_time_limit(bomb_idx):
        _, time_limit = bombs[bomb_idx]
        return time_limit
    
    def get_score(bomb_idx):
        score, _ = bombs[bomb_idx]
        return score
    
    bombs.sort(key=lambda x: (x[1], x[0]))

    pq = []
    bomb_idx = n - 1
    answer = 0

    for t in range(max_t, 0, -1):
        while bomb_idx >= 0 and get_time_limit(bomb_idx) >= t:
            heapq.heappush(pq, -get_score(bomb_idx))
            bomb_idx -= 1

        if pq:
            answer += -heapq.heappop(pq)
    
    print(answer)

solution()