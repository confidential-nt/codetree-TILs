def solution():
    # (i,j) 마다 3 x 3 격자를 탐색
    # 해당 격자에서 1이 몇개인지를 셈 -> 최대 동전 수 갱신

    # 격자 만들 때 바깥으로 안삐져나가는지 먼저 확인 : i + 2, j + 2 >= N 이라면...
    # 격자 어떻게 만듦? -> 그냥 i,j 자리에서 +2 해버리면 되지 않을까
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N):
        for j in range(N):
            if i + 2 >= N or j + 2 >= N:
                continue
            count = 0
            for row in range(i, i+2+1):
                for col in range(j, j+2+1):
                    if matrix[row][col] == 1:
                        count += 1
            max_count = max(max_count, count)
    print(max_count)




solution()