def solution():
    # 추상화 해놓고 보면 결국엔 첫번째 행, 마지막 행을 제외하고 나머지 공간에 두 개의 1x1 크기의 사각형을 어디에 놓을 것인지 결정하는 문제와 같다.
    R,C = map(int, input().split())
    arr = [input().split() for _ in range(R)]
    start = arr[0][0]
    end = arr[R -1][C - 1]
    loc = (0,0)
    count = 0
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            for k in range(i+1, R - 1):
                for l in range(j+1, C - 1):
                    if arr[i][j] != start and arr[k][l] != end and arr[i][j] != arr[k][l]:
                        count += 1
                        
    print(count)









solution()