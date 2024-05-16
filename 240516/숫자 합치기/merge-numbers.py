# 이처럼 순간 순간마다 어떤 쌍을 선택해야 하는지에 대한 판단이 확실히 서는 경우에도 그리디 알고리즘을 사용하여 문제를 해결할 수 있습니다.
from collections import deque


def solution():
    n = int(input())
    arr = deque(list(map(int, input().split())))
    answer = 0
    while len(arr) != 1:
        arr = deque(sorted(arr))
        a = arr.popleft()
        b = arr.popleft()
        answer += a + b
        arr.append(a + b)
       

    print(answer)

solution()