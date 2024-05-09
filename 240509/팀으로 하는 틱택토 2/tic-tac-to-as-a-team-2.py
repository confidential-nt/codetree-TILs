MAX_A = 3
MAX_X = 9

def solution():

    board = [list(map(int, input())) for _ in range(MAX_A)]

    answer = 0

    for i in range(1, MAX_X + 1):
        for j in range(i + 1, MAX_X + 1):
            # 보드를 직접 탐색하는 것보다, 조합에 대해 먼저 생각. (i,j)는 한팀.
            win = False

            num_i = 0
            num_j = 0

            # 가로
            for k in range(MAX_A):
                num_i = 0
                num_j = 0
                for l in range(MAX_A):
                    if board[k][l] == i: # 인덱싱 주목
                        num_i += 1
                    if board[k][l] == j:
                        num_j += 1

                if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                    win = True

            
            # 세로
            for k in range(MAX_A):
                num_i = 0
                num_j = 0
                for l in range(MAX_A):
                    if board[l][k] == i:
                        num_i += 1
                    if board[l][k] == j:
                        num_j += 1
                if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                    win = True
            
            # 오른쪽 대각선
            num_i = 0
            num_j = 0
            for k in range(MAX_A):
                if board[k][k] == i: # 인덱싱 주목
                    num_i += 1
                if board[k][k] == j:
                    num_j += 1
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

            # 왼쪽 대각선
            num_i = 0
            num_j = 0
            for k in range(MAX_A):
                if board[k][MAX_A - k - 1] == i:
                    num_i += 1
                if board[k][MAX_A - k - 1] == j:
                    num_j += 1
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

            if win: # 이렇게 하면 자동으로 중복이 스킵.
                answer += 1    

    print(answer)   


solution()