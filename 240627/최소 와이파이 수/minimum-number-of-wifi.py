def solution():
    # 와이파이를 되도록 뒤에 놓는다 -> 최소로 와이파이를 설치할 수 있도록 -> 되도록 뒤에 넣게 되면, 앞으로 남아 있는 숫자의 수가 줄어들기 때문에 추후에 사용할 칸막이의 수를 더 줄일 가능성이 높아지니까.
    # ** 다만 앞에서부터 모든 사람이 커버가 가능해야한다. **
    # 즉, 되도록 뒤에 놓는데, 거리 m 안에 존재하는 모든 사람을 빠짐없이 커버할 수 있어야함.

    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1

    if count == 0:
        print(0)
        return

    cover = 2 * m + 1
    if cover > n:
        print(1)
        return

    answer = n // cover if m > 0 else count
    print(answer)

solution()