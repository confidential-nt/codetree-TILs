from collections import defaultdict

def solution():
    X,Y = map(int, input().split())
    answer = 0
    for i in range(X, Y + 1):
        num = i
        digit = [0] * 10 # 0 ~ 9
        all_digits = 0
        while num: # 저번에도 그렇고 자릿수 관련한 계산은 이렇게 해보자.
            digit[num % 10] += 1
            all_digits += 1
            num //= 10
        
        interesting = False

        for j in range(10):
            if digit[j] == all_digits - 1: # digit[j]가 all_digits - 1이면 나머지 digit[j]는 1일수 밖에 없음.
                interesting = True

        if interesting:
            answer += 1
    print(answer)    
solution()