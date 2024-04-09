import sys

MIN_VALUE = -sys.maxsize

n,m = map(int, input().split())
board = [
    [0] * m for _ in range(n)
]

arr = [list(map(int, input().split())) for _ in range(n)]

def solution():
    # 이전 제출한 코드의 문제:
    # 1. 직사각형은 두 꼭짓점으로 이루어진 것이라는 것을 간과.
    
    max_score = MIN_VALUE    
    
    for i in range(n): # top-left
        for j in range(m):
            for k in range(i, n): # right-bottom
                for l in range(j, m):
                    max_score = max(max_score, find_max_score(i,j,k,l))
    print(max_score)

def find_max_score(x1,y1,x2,y2):
    max_score = MIN_VALUE

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if is_possible(x1,y1,x2,y2,i,j,k,l):
                        max_score = max(max_score, rect_sum(x1,y1,x2,y2) + rect_sum(i,j,k,l))
    return max_score

def rect_sum(x1,y1,x2,y2):
    return sum([
        arr[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


def is_possible(x1,y1,x2,y2,x3,y3,x4,y4):
    clear_board()
    draw(x1,y1,x2,y2)
    draw(x3,y3,x4,y4)
    # 두 직사각형을 격자에 새로 그렸을 때, (1로 나타냄) 어떤 지점이 2이상이라면 그것은 겹친다는 의미.
    return not check_board()


def draw(x1,y1,x2,y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

solution()