import sys

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    negative, zero, positive = 0,0,0

    arr.sort()
    # 이렇게 미리 양수, 음수, 0의 수를 세는 것이 간단하게 문제를 푸는 키 => 경우를 잘생각해보면 정리해볼 수 있음. 큰 그림처럼 미리 만들어서 정리하는 것.
    for i in range(n):
        if arr[i] < 0:
            negative += 1
        if arr[i] == 0:
            zero += 1
        if arr[i] > 0:
            positive += 1

    # 곱 중 양수가 존재한다 => 이 양수의 값이 가장 최선의 값임. 그리고 이 값은 0보다 무조건 큼.
    # = 양수 3개의 곱 or 양수 1개와 음수 2개의 곱
    if positive >= 3 or (positive >= 1 and negative >=2):
        # 양수가 3개 이상이라면, 그 중 가장 큰 3개의 수를 곱하는 것이 최선
        if positive >= 3:
            answer = max(answer, arr[n - 1] * arr[n - 2] * arr[n - 3])
        # 음수 2개와 양수 1개를 곱할 때에는, 음수 2개는 절댓값이 가장 큰 값을, (즉, 가장 작은 두 값)
        # 양수 1개는 가장 큰 값을 골라 곱하는 것이 최선입니다.
        if positive >= 1 and negative >= 2:
            answer = max(answer, arr[n - 1] * arr[0] * arr[1])
        # 이와 같이 2가지 경우가 동시에 존재할 수 있기 때문에 max를 사용함.   
    # 곱 중 양수가 존재하지 않으며 곱 중 0이 존재할 때 => 그 다음으로 최선의 값임
    elif zero >= 1:
        answer = 0
    # 곱 중 음수만 존재할 때
    # 배열에 -밖에 없거나 / (negative = 1, zero = 0, positive = 2)인 경우
    # 이 경우 가장 절댓값이 작은 값 3개(=가장 큰 값 3개)를 고르는 것이 최선입니다.
    # ex) [-5, -4, -3, -2, -1] / [-5,1,2]
    else:
        answer = arr[n - 1] * arr[n - 2] * arr[n - 3]
    
    print(answer)
# 잘 생각하면 굳이 절댓값을 기준으로 정렬하지 않고도 문제를 풀 수 있음.
solution()