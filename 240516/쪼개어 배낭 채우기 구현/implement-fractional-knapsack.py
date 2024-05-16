# 해당 문제는 Functional Knapsack -> 쪼개어 담을 수 있음. -> 그리디 사용가능.
# 쪼개어 담을 수 없는 문제: 0/1 Knapsack -> dp 사용해야

def solution():
    n,m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    # (무게, 가치)

    arr.sort(key=lambda x: -x[1] / x[0]) # 음수를 이용하여 내림차 순으로 정렬.

    answer = 0
    for w,v in arr:
        if m >= w:
            answer += v
            m -= w
        else:
            answer += v * (m / w)
            break
    print(f"{answer:.3f}")        
solution()