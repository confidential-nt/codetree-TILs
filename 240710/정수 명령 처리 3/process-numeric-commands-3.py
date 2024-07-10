from collections import deque


def solution():
    n = int(input())
    dq = deque()
    for _ in range(n):
        line = input().split()
        if line[0] == "push_back":
            dq.append(int(line[1]))
        if line[0] == "push_front":
            dq.appendleft(int(line[1]))
        if line[0] == "pop_front":
            print(dq.popleft())
        if line[0] == "pop_back":
            print(dq.pop())
        if line[0] == "front":
            print(dq[0])
        if line[0] == "back":
            print(dq[-1])
        if line[0] == "size":
            print(len(dq))
        if line[0] == "empty":
            print(int(not dq))
        
solution()