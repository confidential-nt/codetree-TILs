# 주어진 수열에서 뒷부분에 있는 정렬된 부분을 제외하고, 그 외의 앞부분을 뒤의 적절한 자리에 잘 삽입하라.
# 정렬되지 않은 앞부분의 원소를 정렬된 뒷부분 사이사이에 적절히 끼워넣으면 되므로, 답은 정렬되어 있지 않은 원소의 개수임.
# 따라서 뒤에서부터 보며 정렬되어있지 않은 순간을 잡아 그 앞에 있는 원소의 개수가 답이 됨.
def solution():
    # 1이상 n이하의 다 다른 n개의 숫자로 구성된 수열.
    # 맨 앞에 있는 숫자를 중간에 집어넣음.

    # 맨 뒤에 있는 숫자들이 
    # 정렬된 상태로 가장 길게 놓여져 있는 것이 좋습니다.
    # 예를 들어 1 3 6 5 2 4 7 라는 수열이 있다면
    # 2 4 7은 이미 정렬되어 있으므로
    # 앞에 있는 1 3 6 5만 각 위치에 잘 옮겨주면 됩니다.
    # 따라서 4가 됩니다.

    n = int(input())
    blocks = list(map(int, input().split()))

    idx = n - 2
    while idx >= 0 and blocks[idx] < blocks[idx + 1]:
        idx -= 1

    print(idx + 1)

solution()

# 1 2 4 5 3
# 2 4 5 1 3
# 4 5 1 2 3
# 5 1 2 3 4
# 1 2 3 4 5

# 1이고, 정렬이 안되어있을 경우, 가장 차이가 덜 나는 숫자 앞으로 와야함
# n이고, 정렬이 안되어있을 경우, 맨 마지막으로 가야함.