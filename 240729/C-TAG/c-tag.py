from itertools import combinations

def solution():
    n,m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    count = 0
    
    for x,y,z in combinations(range(m), 3):
        s = set()
        for i in range(n):
            a1 = a[i][x] + a[i][y] + a[i][z]
            s.add(a1)

        is_possible = True
        for i in range(n):
            b1 = b[i][x] + b[i][y] + b[i][z]
            if b1 in s:
                is_possible = False
                break
        
        if is_possible:
            count += 1
            
    print(count)

solution()

# 조건을 잘못이해한듯.. 같은 문자열이 그 어느곳에서도 있어선 안됨 (위치와 관계없이. 나는 위치가 다르면 ㄱㅊ은줄.)
# 뭔가 이 문제와 같이 조건을 확신하지 못하겠다면 헷갈리는 그 모든 조건에 대하여 계산을 해봐야할듯