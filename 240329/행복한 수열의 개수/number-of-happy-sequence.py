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
    # 행
    for i in range(n):
        for j in range(n):
            if j + n - 1 >= n:
                continue
            before = 0
            count = 0
            end = False
            for col in range(n):
                current = arr[i][col]
                if current == before:
                    count += 1
                else:
                    if count >= m: # 이미 만족했다면 더 이상 셀 필요가 없음. 이미 그 수열은 답에 포함됨.
                        answer += 1
                        end = True
                        break
                    before = current
                    count = 1  
            if not end and count >= m:
                answer += 1

    # 열
    for i in range(n): # 행 -> 고정
        for j in range(n): # 열 -> 변화
            if i + n - 1 >= n:
                continue
            count = 0  
            before = 0
            end = False  
            for row in range(n):
                current = arr[row][j]
                if current == before:
                    count += 1
                else:
                    if count >= m:
                        answer += 1
                        end = True
                        break
                    before = current
                    count = 1
            if not end and count >= m :
                answer += 1
            
    print(answer)

solution()