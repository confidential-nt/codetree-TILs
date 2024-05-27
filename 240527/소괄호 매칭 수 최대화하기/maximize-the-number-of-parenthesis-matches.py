from functools import cmp_to_key

def solution():
    n = int(input())
    brackets = []

    ans = 0

    for _ in range(n):
        s = input() # 이 각각의 n개의 s의 길이의 합은 50만을 넘기지 않는다. = 처음에 각각의 모든 s가 50만 이하라는 줄 알았음. -> 문제 못 푼 이유;
        open_num, closed_num = 0,0
        for char in s:
            if char == "(":
                open_num += 1
            else:
                closed_num += 1
                # 해당 문자열 만으로 얻게 되는 점수는
                # 미리 답에 더해줍니다.
                ans += open_num # open_num의 개수만큼 점수가 더해짐. 그만큼 짝이 지어질 수 있는것이니까.
        
        # 이렇게 하는 이유: 문자열을 조정해가면서 뭐가 더 큰 점수를 내는지 알아내야 하는데(완탐)
        # 그렇게 하려면 괄호 문자열의 총 길이는 50만이므로 시간 초과.
        # 이런 식으로 숫자를 도출해서 정렬을 이용함으로써
        # 빠른 계산을 모색.
        brackets.append((open_num, closed_num))
    
    brackets.sort(key=cmp_to_key(compare)) # 이렇게 정렬을 하면 각각의 문자열들을 붙여봤을 때 가장 큰 점수를 내는 최종 괄호 문자열을 도출해낼 수 있음.

    open_sum = 0
    for open_num, closed_num in brackets:
        # 이러면 첫 루프에서는 ans에 0이 더해지게 됨 -> 당연. 처음엔 해당 문자열 내 이미 짝지어진 괄호 문자열이 있는 경우 말고는 점수를 낼 수 없기 때문. 얘가 첫 시작이기 때문에.
        ans += open_sum * closed_num

        open_sum += open_num

    print(ans)
            

def compare(b1, b2):
    open1, closed1 = b1
    open2, closed2 = b2

    # b1,b2 / b2,b1 둘다 붙여본다. 더 큰것을 앞에 오도록 한다.
    # 붙였을 때 더 큰 점수를 내는 것을 파악.
    # 괄호의 개수로 간접적으로 더 큰 점수를 내는 것을 파악할 수 있음.
    if open1 * closed2 > open2 * closed1:
        return -1

    if open1 * closed2 < open2 * closed1:
        return 1

    return 0

solution()