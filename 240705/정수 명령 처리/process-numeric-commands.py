class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]

def solution():
    n = int(input())
    stack = Stack()
   
    for _ in range(n):
        line = input().split()
        command = line[0]
        number = None
        if len(line) > 1:
            number = int(line[1])
        
        if command == "push":
            stack.push(number)
        if command == "pop":
            print(stack.pop())
        if command == "size":
            print(stack.size())
        if command == "empty":
            print(int(stack.empty()))
        if command == "top":
            print(stack.top())

solution()