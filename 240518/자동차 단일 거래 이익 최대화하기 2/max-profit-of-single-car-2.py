def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    max_profit = 0
    min_price = arr[0]

    for i in range(n):
        # 자동차를 파는 시점을 기준으로 그 전에 언제 자동차를 샀어야 하는지를 생각해보는 것.
        # 자동차를 사야 하는 시점: 파는 시점을 기준으로 앞선 해의 최솟값일 때 구매를 했을 때.
        # 단, 시간복잡도를 위해 최솟값 갱신도 같이 함 -> 문제의 특성 때문에 가능.
        profit = arr[i] - min_price

        if profit > max_profit:
            max_profit = profit
        
        if min_price > arr[i]:
            min_price = arr[i]

    print(max_profit)

    

solution()