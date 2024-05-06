def solution():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for i in range(1,4):
        # i번 종이컵을 처음 조약돌을 넣을 종이컵으로 선택합니다.
        current = [0,0,0,0]
        current[i] = 1
        score = 0
        for j in range(N):
            choice = arr[j]
            a = choice[0]
            b = choice[1]
            c = choice[2]
            temp = current[a]
            current[a] = current[b]
            current[b] = temp
            if current[c] == 1:
                score += 1
        max_score = max(max_score, score)


    print(max_score)
solution()