from collections import deque

def solution():
    n = int(input())
    dq = deque(range(1,n+1))
    while len(dq) != 1:
        dq.popleft()
        front = dq.popleft()
        dq.append(front)
    print(dq[-1])


solution()