n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution():
    # 직사각형은 (i,j) (k,l)로 이루어짐
    # 모든 좌표를 돌면서 각각의 직사각형 안에 들어있는 값이 전부다 양수이냐
    # 동시에 직사각형의 크기를 세는 것.
    # max 갱신
    # 하나라도 음수가 나오면 갱신 안함.
    # 초깃값: -1로 세팅
    answer = -1
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if is_all_positive(i,j,k,l):
                        answer = max(answer, count_size(i,j,k,l))
    print(answer)

                    
    
def is_all_positive(x1,y1,x2,y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if arr[x][y] < 0:
                return False
    return True

def count_size(x1,y1,x2,y2):
    count = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            count += 1
    return count
solution()