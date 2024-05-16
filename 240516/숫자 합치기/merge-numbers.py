# 이처럼 순간 순간마다 어떤 쌍을 선택해야 하는지에 대한 판단이 확실히 서는 경우에도 그리디 알고리즘을 사용하여 문제를 해결할 수 있습니다.
# 매번 최소를 선택하는 문제엔 우선순위큐가 좋은듯.
import heapq


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    pq = []
    answer = 0

    for el in arr:
        heapq.heappush(pq, el)

    while len(pq) != 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        answer += (a + b)
        heapq.heappush(pq, a + b)
       

    print(answer)

solution()