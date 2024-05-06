def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    min_val = float("inf")
    for i in range(n):
        arr[i] *= 2
        for j in range(n):
            # 제외할 숫자
            new_arr = []
            for k in range(n):
                new_arr = [el for index, el in enumerate(arr) if index != j]


            sum_res = 0
            for k in range(n - 2):
                sum_res += abs(new_arr[k + 1] - new_arr[k])
            min_val = min(sum_res, min_val)



        arr[i] //= 2
    print(min_val)

solution()