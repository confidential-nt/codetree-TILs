def solution():
    N,K = map(int, input().split())
    
    placed = [0] * 101
    # 사탕의 개수, 바구니의 좌표
    for _ in range(N):
        num_of_candy, coord = map(int, input().split())
        placed[coord] += num_of_candy

    max_count = 0
    for c in range(1,101): # 중심점
        count = 0
        for j in range(c - K , c + K + 1):
            if j >=0 and j < 101:
                count += placed[j]
        max_count = max(max_count, count)    
            
    print(max_count)        



solution()