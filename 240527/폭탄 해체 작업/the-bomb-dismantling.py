import heapq

def solution():
    # 난 틀림 -> 이 문제에서 말한대로 시간제한이 증가하는 순으로 선택했기 때문. -> 반례가 존재.
    # 그게 아니라 시간제한이 감소하는 순으로 보며, 해당 시간에 선택할 수 있는 폭탄 중 가장 점수가 높은 폭탄을 선택해야함
    # 느낌적인 느낌으로 시간 제한이 감소하는 순으로 봐야 모든 경우의 수를 보면서 최대인 점수를 가지는 것을 다룰 수 있기 때문.
 
    n = int(input())
    bombs = [tuple(map(int, input().split())) for _ in range(n)]
    max_t = max([el[1] for el in bombs])

    def get_time_limit(bomb_idx):
        _, time_limit = bombs[bomb_idx]
        return time_limit
    
    def get_score(bomb_idx):
        score, _ = bombs[bomb_idx]
        return score
    
    bombs.sort(key=lambda x: (x[1], x[0])) # 시간 - 점수 기준으로 오름차순으로 정렬.

    pq = []
    bomb_idx = n - 1
    answer = 0

    # 남은 제한 시간을 들여다 보는 것과 같다.
    # max_t에서 1초씩 줄어든다.
    for t in range(max_t, 0, -1):
        # 제한 시간이 t 만큼 남았을 때, 아직 시간이 여유로운 폭탄들을 모두 찾는다. (해당 시간에 제거할 수 있는 폭탄들을 모두 찾는다.) => 그냥 모든 폭탄을 본다.
        while bomb_idx >= 0 and get_time_limit(bomb_idx) >= t:
            heapq.heappush(pq, -get_score(bomb_idx))
            bomb_idx -= 1

        if pq:
            # 폭탄이 있으면 그 폭탄들 중에서 가장 높은 점수를 가지는 폭탄을 제거한다. -> 한 시간에 하나씩만 제거 가능하므로 가장 큰 점수를 얻을 수 있는 것을 제거해야함.
            answer += -heapq.heappop(pq)
            # 주의: 또 시간적 순서와는 관계없음. 그냥 가장 높은 점수를 가지는 폭탄을 제거하는 것. 가장 높은 초부터 1초까지 살펴보는 이유. 1초 남은 폭탄도 높은 점수를 가진다면 제거 될 것.
    print(answer)

solution()