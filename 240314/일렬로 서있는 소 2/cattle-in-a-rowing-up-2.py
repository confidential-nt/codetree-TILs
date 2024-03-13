def solution():
    n = int(input())
    height = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k and height[i] <= height[j] <= height[k]:
                    count += 1
    print(count)
solution()