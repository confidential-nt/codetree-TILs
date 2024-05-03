def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    max_count = 0

    for h in range(1, 1001):
        count = 0
        # 가장 왼쪽에 빙산이 있는 경우의 예외를 처리
        if arr[0] > h :
            count += 1

        # 바로 앞 블록은 해수면에 잠겨있고
        # 자기 자신의 블록은 해수면 위에 떠있는 경우,
        # 자기 자신 블록부터 시작하는 빙산이 하나 더 있습니다. -> 이 사실을 못깨달았네..
        # 나는 while문을 썼는데 실수할 위험이 큼 -> 이보다 정확한 공식이 있을 수도 있다. 이 문제처럼.
        for i in range(1, n):
            if arr[i - 1] <= h and arr[i] > h:
                count += 1
        max_count = max(count, max_count)        
    print(max_count)
solution()