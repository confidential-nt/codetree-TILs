def solution():
    n = int(input())

    changes = [
        input().split()
        for _ in range(n)
    ]

    score_a, score_b, score_c = 0,0,0

    def get_status(score1, score2,score3):
        # A만, B만, C만, (A,B)/ (A,C)/ (B,C)/ (A,B,C)
        if score1 > score2 and score1 > score3:
            return 1
        elif score2 > score1 and score2 > score3:
            return 2
        elif score3 > score1 and score3 > score2:
            return 3
        elif score1 == score2 and score1 > score3:
            return 4
        elif score1 == score3 and score1 > score2:
            return 5
        elif score2 == score3 and score2 > score1:
            return 6
        else:
            return 7

    
    ans = 0
    # 순서대로 점수를 변동시켜보며
    # 조합이 몇 번 변동되는지를 조사합니다.
    for name, value in changes:
        value = int(value)
        # 변동이 있는 학생이 A라면
        if name == 'A':
            # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
            # 답을 갱신합니다.
            if get_status(score_a, score_b,score_c) != get_status(score_a + value, score_b, score_c):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_a += value

        # 변동이 있는 학생이 B라면
        elif name == "B":
            # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
            # 답을 갱신합니다.
            if get_status(score_a, score_b,score_c) != get_status(score_a, score_b + value, score_c):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_b += value
        else:
            if get_status(score_a, score_b,score_c) != get_status(score_a, score_b, score_c + value):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_c += value
    print(ans)
solution()


def soluton2():
    # 구분 짓는 과정을 좀 더 간단하게 축소해버릴 수 있음.
    # 변수 선언 및 입력:
    n = int(input())

    # 입력받은 학생 이름과 점수 변동값을 저장합니다.
    changes = [
        input().split()
        for _ in range(n)
    ]

    # 현재 A, B의 점수를 나타냅니다.
    score_a, score_b, score_c = 0, 0, 0


    # 명예의 전당 상태를 반환합니다.
    # 총 7가지 상황이 있습니다.
    def get_status(score1, score2, score3):
        return_val = 0
        maxval = max([score1, score2, score3]) 
        
        # 다음과 같이 하면 상태들을 서로 겹치지 않고 정리할 수 있습니다.
        # 1. A가 명예의 전당에 올라가 있는 경우 상태에 1을 더합니다.
        if score1 == maxval:
            return_val += 1

        # 2. B가 명예의 전당에 올라가 있는 경우 상태에 2를 더합니다.
        if score2 == maxval:
            return_val += 2
        
        # 3. C가 명예의 전당에 올라가 있는 경우 상태에 4를 더합니다.
        if score3 == maxval:
            return_val += 4
        
        return return_val


    ans = 0
    # 순서대로 점수를 변동시켜보며
    # 조합이 몇 번 변동되는지를 조사합니다.
    for name, value in changes:
        value = int(value)
        # 변동이 있는 학생이 A라면
        if name == 'A':
            # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
            # 답을 갱신합니다.
            if get_status(score_a, score_b, score_c) != get_status(score_a + value, score_b, score_c):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_a += value

        # 변동이 있는 학생이 B라면
        elif name == 'B':
            # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
            # 답을 갱신합니다.
            if get_status(score_a, score_b, score_c) != get_status(score_a, score_b + value, score_c):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_b += value
        
        # 변동이 있는 학생이 C라면
        else:
            # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
            # 답을 갱신합니다.
            if get_status(score_a, score_b, score_c) != get_status(score_a, score_b, score_c + value):
                ans += 1
            
            # 값을 갱신해줍니다.
            score_c += value

    print(ans)