def solution():
    n = int(input())
    people = list(map(int, input().split()))
    result = float("inf")
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += people[j] * abs((j - i))
        result = min(result, sum)    
    print(result)

solution()