# 평평하게 균형을 맞추는 문제.
# 항상 평균보다 많은 블록 -> 적은 블록으로 옮기면 됨.

def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    avg = sum(arr) // n

    answer = 0
    for i in range(n):
        if arr[i] < avg:
            answer += (avg - arr[i])
    print(answer)
solution()