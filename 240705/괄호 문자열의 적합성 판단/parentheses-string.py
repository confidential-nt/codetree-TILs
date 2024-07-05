from collections import deque

def solution():
    stack = deque()
    string = list(input())
    n = len(string)
    for i in range(n):
        char = string[i]

        top = stack[-1]
        
        if char == "(": # (인 경우엔 무조건 넣음.
            stack.push(char)
        else: # ) 인데 스택이 비어있다면, 올바른 괄호 될 가망 없음.
            if not stack:
                print("No")
                return
            else: # ) 가 첫번째 원소로 들어올리가 없으므로 비어있지 않다면 그건 무조건 ).
                stack.pop()

    if len(stack):
        print("No")
    else:
        print("Yes")
    

solution()