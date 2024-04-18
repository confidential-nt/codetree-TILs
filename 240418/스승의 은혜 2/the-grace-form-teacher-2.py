def solution():
    N,B = map(int, input().split())
    P = [int(input()) for _ in range(N)]
    max_count = 0
    for i in range(N):
        tmp = [P[j] for j in range(N)]
        tmp[i] /= 2

        # 정렬;; 그리디 문제 아니여 이거;;
        tmp.sort()
        count = 0
        total = 0

        for j in range(N):
            if total + tmp[j] <= B:
                total += tmp[j]
                count += 1
        max_count = max(count, max_count)
    print(max_count)
solution()