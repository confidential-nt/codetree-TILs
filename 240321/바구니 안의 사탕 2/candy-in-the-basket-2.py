def solution():
    N,K = map(int, input().split())
    
    placed = [0] * 101
    # 사탕의 개수, 바구니의 좌표
    for _ in range(N):
        num_of_candy, coord = map(int, input().split())
        placed[coord] += num_of_candy

    max_count = 0
    for c in range(101 - K): # 중심점
        if c - K < 0 :
            continue
        arr = placed[c - K:c + K + 1]
        count = 0
        for el in arr:
            count += el
        max_count = max(max_count, count)    
            
    print(max_count)        



solution()