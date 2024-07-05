from collections import deque

def solution():
    stack = deque()
    string = list(input())
    n = len(string)
    for i in range(n):
        char = string[i]
        if not len(stack):
            stack.append(char)
            continue

        top = stack[-1]
        
        if top == "(":
            if char == ")":
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    
    if len(stack):
        print("No")
    else:
        print("Yes")
    

solution()