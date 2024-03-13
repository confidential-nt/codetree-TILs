def solution():
    n = int(input())
    people = list(map(int, input().split()))
    result = float("inf") # 그냥 최소값을 구하면 되는것이므로 배열에 저장할 필요 x.
    for i in range(n):
        sum = 0 
        for j in range(n):
            sum += people[j] * abs((j - i)) # j == i 면 어차피 0 이니까 분기처리 필요 x.
        result = min(result, sum)    
    print(result)

solution()