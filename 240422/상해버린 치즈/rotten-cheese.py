def solution():
    N,M,D,S = map(int, input().split())
    eat_logs = [list(map(int, input().split())) for _ in range(D)]
    sick_logs = [list(map(int, input().split())) for _ in range(S)]

    max_count = 0

    # 1. 치즈를 하나씩 돈다.
    # 2. 가능한지 판단한다. (아픈 사람의 목록과 매치되는지 => 얘가 이 치즈를 먹었니?)
    # 3. 가능하지 않으면 다음 치즈로 넘어간다.
    # 4. 가능하면 해당 치즈를 먹은 사람의 수를 파악한다 -> 최대 필요한 약의 수를 갱신한다.
    # 질문: 정렬이 필요한가? 시간 순에 따른 정렬? 치즈 순서에 따른 정렬?
    # 고려사항: 시간도 중요. 아파지기 전에 먹어야 상한 치즈임.
    # 고려사항: 아픈 사람 기록에는 모든 아픈 사람이 포함되지 않기 때문에 상한 치즈로 인해 아플 수도 있는 사람까지 포함시켜야.
    for cheeze in range(1, M+1): # 이게 상한치즈라면
        
        re = [0] * (N + 1)
        for p,m,t in eat_logs:
            if m != cheeze:
                continue
            if not re[p]:
                re[p] = t
            elif re[p] > t: # 이 부분 주의. 같은 치즈를 여러번 먹는 입력도 나오나봄..?
                re[p] = t    
        
        is_possible = True
        for p,t in sick_logs:
            if re[p] >= t or not re[p]:
                is_possible = False
                break

        count = 0
        if is_possible:
            for r in re:
                if r:
                    count += 1
            
        max_count = max(count, max_count)        



    print(max_count)


solution()