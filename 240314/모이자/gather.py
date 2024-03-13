def solution():
    n = int(input())
    people = list(map(int, input().split()))
    result = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            result[i] += people[j] * abs((j - i))
    print(min(result))

solution()