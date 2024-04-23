def solution():
    K,N = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(K)]
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            

            is_immutable = True
            for score in scores:
                # 이렇게 하는 게 더 간단한지도? combinations보다. 결국 중요한 것은 위치 비교.
                index_a = score.index(i)
                index_b = score.index(j)

                if index_a > index_b:
                    is_immutable = False
                    break
            
            if is_immutable:
                count += 1

    print(count)




solution()