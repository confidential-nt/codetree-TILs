from collections import deque

def solution():
    n,k = map(int, input().split())
    queue = deque(range(1,n+1))
    
    index = 0
    while queue:
        for _ in range(k - 1):
            front = queue.popleft()
            queue.append(front)
        print(queue.popleft(), end=" ")

solution()

# 5 6 1 2 3
#