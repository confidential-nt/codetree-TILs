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