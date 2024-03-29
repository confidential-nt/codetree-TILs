def solution():
    # (i,j)로 격자의 좌표 타고 다님
    # 행, 열 수열 따로 탐색
    # 각각 열,행쪽 좌표가 n보다 크거나 같은지 확인
    # 연속으로 m개 이상 같은 숫자가 등장하는지 확인.

    # 고려 사항
    # 연속으로 m개이상 같은 숫자가 등장하는지 어떻게 확인? 
    # 행의 경우: i고정, 열의 경우 n까지 루프. -> before, current를 통해 숫자 비교 -> 같다면 count += 1 / 다르다면 count 냅두거나 1로 초기화
    # + 주의 : 끊기는 지점에서 연속된 숫자가 몇 번 나왔는지 count를 한번 살펴봐야 함.
    # 주의: 연속되는 수의 개수를 구하는 게 아니라, 단지 m개 이상의 연속된 수가 나오는 수열을 구하는 것임.

    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    seq = [0 for _ in range(n)]
    # 행
    for i in range(n):
        seq = arr[i][:]
        count = 1
        max_count = 1
        for j in range(1,n):
            if seq[j - 1] == seq[j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count) # 결국 최대를 구하면 됨.
        if max_count >= m :
            answer += 1            
       
    # 열
    for j in range(n):
        for i in range(n):
            seq[i] = arr[i][j] # 답을 구하기 쉽게 데이터의 형태를 변형
        count = 1
        max_count = 1
        for k in range(1,n):
            if seq[k - 1] == seq[k]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count) # 반복문 안에 포함 -> 이어지다 끊기는 경우도 커버 가능.
        if max_count >= m :
            answer += 1            
             
        
    print(answer)
solution()