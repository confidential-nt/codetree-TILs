def solution():
    n = int(input())
    # i(5원 동전의 수) 를 0부터 100000까지 해서 반복문을 돌아서 구할 수도 있음
    # 어쨌든 중요한 포인트는 5원을 최대한 많이 쓰는게 최적의 답이라는 것.

    coin_count = n // 5

    while coin_count >= 0:
        remain = n - coin_count * 5

        if remain % 2 == 0:
            coin_count += remain // 2
            print(coin_count)
            break
        
        coin_count -= 1
            
    if coin_count < 0:
        print(-1)


solution()