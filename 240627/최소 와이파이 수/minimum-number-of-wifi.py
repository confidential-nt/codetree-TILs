def solution():
    # 와이파이를 되도록 뒤에 놓는다 -> 최소로 와이파이를 설치할 수 있도록 -> 되도록 뒤에 넣게 되면, 앞으로 남아 있는 숫자의 수가 줄어들기 때문에 추후에 사용할 칸막이의 수를 더 줄일 가능성이 높아지니까.
    # ** 다만 앞에서부터 모든 사람이 커버가 가능해야한다. **
    # 즉, 되도록 뒤에 놓는데, 거리 m 안에 존재하는 모든 사람을 빠짐없이 커버할 수 있어야함.

    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    last = arr
    answer = 0
    while True:
        start = -1
        n = len(last)

        for i in range(n):
            if last[i] == 1:
                start = i
                break
        
        if start == -1:
            print(answer)
            break
        
        last = last[2*m + start + 1:]
        answer += 1


solution()


def solution2():
    # 변수 선언 및 입력:
    n, m = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))

    # 사람이 살고 있는 곳이 나오면
    # 와이파이를 해당 위치로부터 오른쪽으로 m만큼 떨어진 곳에 놓은 뒤,
    # 2m만큼 떨어진 곳에서 시작하여 다시 탐색을 진행합니다.
    # 배열을 복사할 필요 없이 인덱스 만으로도 해결가능....
    # 문제에서 가장 중요한 것은 1이 어디서 시작하냐는 것이고 그 인덱스만을 기반으로 하면
    # 답이 나옴.
    cnt, i = 0, 0
    while i < n:
        if arr[i] == 1:
            cnt += 1
            i += 2 * m + 1
        else:
            i += 1

    print(cnt)