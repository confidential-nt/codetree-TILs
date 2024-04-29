from collections import defaultdict

def solution():
    X,Y = map(int, input().split())
    answer = 0
    for i in range(X, Y + 1):
        num = i
        digit = [0] * 10 # 0 ~ 9
        all_digits = 0
        while num:
            digit[num % 10] += 1
            all_digits += 1
            num //= 10
        
        interesting = False

        for j in range(10):
            if digit[j] == all_digits - 1:
                interesting = True

        if interesting:
            answer += 1
    print(answer)    
solution()