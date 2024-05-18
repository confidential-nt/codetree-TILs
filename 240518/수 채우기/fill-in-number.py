def solution():
    n = int(input())

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