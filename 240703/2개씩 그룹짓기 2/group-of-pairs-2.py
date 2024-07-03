# n개의 그룹으로 만들어
# 각 그룹내의 2개의 수의 차이 중
# 최솟값이 최대가 되도록 하는

import sys

si = sys.stdin.readline

# 1 <= n <= 100,000 -> n^2 만 해도 100억 이중 포문 풀이로 불가능
n = int(si())

arr = [0] + list(map(int, si().split()))

# 2n 개의 원소를 n개의 그룹으로 쪼개기 
# 두 원소의 차이의 최솟값을 최대로 하기 위해선...
# 차이의 최솟값을 최대..

arr.sort()

# print(arr)
# 2 5 7 9 10 15

# (1, n + 1) (2, n + 2) ... 이런식으로 짝지으면 되나?

min_diff = sys.maxsize 
for i in range(1, n + 1):
    min_diff = min(min_diff, arr[n + i] - arr[i])

print(min_diff)