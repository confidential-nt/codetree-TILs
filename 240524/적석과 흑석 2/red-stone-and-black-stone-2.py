from sortedcontainers import SortedSet
# treeset.
# set(중복 허용 x) + 바로 정렬 및 자동 정렬(생성, 추가, 삭제 시) + 이진 검색 + 순차접근(인덱스)
# BST가 베이스이므로 삭제, 삽입 시에도 빠름.

def solution():
    # A <= T <= B
    # 검은돌의 B의 값이 작은 돌부터 보며 A보다 같거나 큰 빨간돌 중 T 값이 가장 작은 돌을 매칭해주는 것이 
    # 항상 유리함. -> 그래야 가장 많이 쌍을 매칭할 수 있음.
    c,n = map(int, input().split())
    red_stones = [int(input()) for _ in range(c)]

    black_stones = []
    for _ in range(n):
        a,b = tuple(map(int, input().split()))
        black_stones.append((b,a))

    
    red_s = SortedSet(red_stones) # 이진 검색의 이점 위해 사용하는 것.
    # Aj보다 같거나 큰 최소 Ti값을 빠르게 찾기 위해
    # treeset을 이용합니다.

    black_stones.sort() # 검은돌의 B의 값이 작은 돌부터 보며... -> b 기준으로 정렬

    ans = 0
    for b,a in black_stones:
        idx = red_s.bisect_left(a) 
        # bisect_left(value)는 value를 삽입할 수 있는 가장 왼쪽(작은) 위치를 반환합니다. 만약 value가 이미 SortedSet에 존재한다면, bisect_left(value)는 value의 첫 번째 인덱스를 반환합니다. 이는 value보다 작거나 같은 값 중 가장 큰 값의 바로 다음 위치를 의미합니다.
        # bisect_right(value)는 value를 삽입할 수 있는 가장 오른쪽(큰) 위치를 반환합니다. 만약 value가 이미 SortedSet에 존재한다면, bisect_right(value)는 value의 마지막 인덱스 다음 위치를 반환합니다. 이는 value보다 큰 값 중 가장 작은 값의 바로 앞 위치를 의미합니다.

        if idx != len(red_s): # 이 경우 a보다 큰 값이 없다는 의미.
            ti = red_s[idx]
            
            if ti <= b:
                ans += 1
                red_s.remove(ti)

    print(ans)
solution()