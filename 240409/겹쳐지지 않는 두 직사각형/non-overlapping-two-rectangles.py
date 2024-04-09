import sys

def solution():
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_score = -sys.maxsize
    for i in range(n):
        for j in range(m):
            # 시작점 1 (i,j)
            for h_a in range(1,n):
                for w_a in range(1,m):
                    # 시작점 2 (l,k)
                    for l in range(n):
                        for k in range(m):
                            for h_b in range(1,n):
                                for w_b in range(1,m):
                                    # 1. 각 영역이 겹치지 않는지 확인 -> 경계가 있고 그 경계를 넘는가? -> 시작점으로 파악
                                    # -> 이 부분이 핵심인듯.
                                    if (abs(l - i) < h_a and abs(k - j) < w_a):
                                        continue
                                    # 2. index out of range 체크
                                    if i + h_a > n or j + w_a > m or l + h_b > n or k + w_b > m:
                                        continue
                                    # 3. 겹치지 않는다면 각 영역에서의 점수 획득
                                    a_score = 0
                                    for one in range(i, i + h_a):
                                        for two in range(j, j + w_a):
                                            a_score += arr[one][two]
                                    b_score = 0
                                    for one in range(l, l + h_b):
                                        for two in range(k, k + w_b):
                                            b_score += arr[one][two]
                                    # 4. 점수 합 구하기.
                                    max_score = max(max_score , a_score + b_score)
    print(max_score)


solution()