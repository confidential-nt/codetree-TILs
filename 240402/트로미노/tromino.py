def solution():
    n,m = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    trominoes = [
        [(0,0),(0,1),(1,0)], # ㄴ
        [(0,0),(1,0),(2,0)] # ㅡ
    ]
    max_score = 0
    for i in range(n):
        for j in range(m):
            for tromino in trominoes:
                for _ in range(2): # flip
                    for _ in range(4): # rotate
                        max_score = max(max_score, get_max_score(i,j,tromino,n,m,matrix))
                        tromino = rotate(tromino)
                    tromino = flip(tromino)
    print(max_score)
def rotate(tetromino): # 90도 회전
  return [(y, -x) for x, y in tetromino]

def flip(tetromino):
  # 어느 방향으로 대칭시킬 건지 일관된 기준만 세우면 되는듯? 이것은 x축 대칭.
  return [(-x, y) for x, y in tetromino]

def get_max_score(x,y,tromino,n,m,matrix):
    score = 0
    for dx,dy in tromino:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            score += matrix[nx][ny]
        else:
            return 0    
    return score



solution()