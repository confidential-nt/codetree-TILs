def solution():
    N,K = map(int, input().split())
    seq = [int(input()) for _ in range(N)]
    max_bomb_number = -1

    for i in range(N):
        bomb_number = -1
        for j in range(i+1, N):
            if seq[i] == seq[j] and j - i <= K:
                bomb_number = seq[i]
        max_bomb_number = max(bomb_number, max_bomb_number)        



    print(max_bomb_number)

solution()