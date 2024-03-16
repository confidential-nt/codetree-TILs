def solution():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    min_distance = float("inf")
    for i in range(N): # i번째에서 시작한다.
        dist = 0 # 거리를 계산한다
        for j in range(N):
            if j - i > 0:
                dist += arr[j] * (j - i)
            elif j - i < 0:
                dist += arr[j] * (N - 1 - i + abs(j - i))    
        min_distance = min(min_distance, dist)    
    print(min_distance) 
    

solution()