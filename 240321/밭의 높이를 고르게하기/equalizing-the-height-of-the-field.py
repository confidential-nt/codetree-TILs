def solution():
    N,H,T = map(int, input().split()) # 연속하게 최소 T번 이상 H 높이
    field = list(map(int, input().split()))

    min_price = float("inf")

    for i in range(N - T - 1):
        price = 0
        for j in range(i, i + T):
            price += abs(field[j] - H)
        min_price = min(price, min_price)
    print(min_price)

solution()