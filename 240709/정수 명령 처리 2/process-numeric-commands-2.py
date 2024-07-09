from collections import deque

class Queue:
    def __init__(self):          # 빈 큐 하나를 생성합니다.
        self.dq = deque()
                
    def push(self, item):        # 큐의 맨 뒤에 데이터를 추가합니다.
        self.dq.append(item)
                
    def empty(self):             # 큐가 비어있으면 True를 반환합니다.
        return not self.dq
                
    def size(self):              # 큐에 들어있는 데이터 수를 반환합니다.
        return len(self.dq)
        
    def pop(self):               # 큐의 맨 앞에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Queue is empty")
            
        return self.dq.popleft()
                
    def front(self):             # 큐의 맨 앞에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Queue is empty")
                        
        return self.dq[0]


def solution():
    n = int(input())
    lines = [input() for _ in range(n)]
    queue = Queue()
    for line in lines:
        command = line.split()[0]
        if command == "push":
            queue.push(int(line.split()[1]))
        if command == "pop":
            print(queue.pop())
        if command == "size":
            print(queue.size())
        if command == "empty":
            print(int(queue.empty()))
        if command == "front":
            print(queue.front())


solution()