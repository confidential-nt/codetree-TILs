def solution():
    # 2 5 7 9 10 15
    # 예제 관찰 -> 2개의 수 차이 중 최솟값이 최대가 되도록... -> 정렬 후 n만큼 떨어진 사람끼리 묶는 것이 최선
    # 틀린 이유: 이 사실 관찰 못함.
    # 그룹으로 묶인 두 사람이 너무 가까이 있으면 차이가 너무 작아져 최대를 만들기 어려워지고
    # 그렇다고 두 사람이 너무 멀리있다면 남은 사람들끼리 차이를 크게 만들기가 어려움
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = float("inf")
    for i in range(n):
        # 이미 최대가 되는 조합
        diff = arr[i + n] - arr[i]
        answer = min(answer, diff)
    print(answer)

solution()