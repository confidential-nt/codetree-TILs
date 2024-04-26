def solution():
    X,Y = map(int, input().split())

    max_sum = 0
    for num in range(X,Y+1):
        nums = [int(el) for el in str(num)]
        sum_res = sum(nums)
        max_sum = max(max_sum, sum_res)
    print(max_sum)
solution()