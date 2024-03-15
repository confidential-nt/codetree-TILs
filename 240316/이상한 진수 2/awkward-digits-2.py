def solution():
    a = list(map(int, list(input())))
    length = len(a)

    max_number = 0
    for i in range(length):
        a[i] = 1 - a[i]

        num = 0
        for j in range(length):
            # num * 2 : 현재까지의 num 값에 2를 곱함으로써, 이진수에서 한 자리를 왼쪽으로 이동시키는 것.
                # 즉, 이진수의 다음 자릿수를 처리할 준비를 하는 것 -> ex) 10에서 한자리를 왼쪽으로 이동시키면 100이 됨. 2배.
            # + a[j] :  현재 자릿수의 값을 더하는 것. 
                # 이진수에서는 각 자릿수가 0 또는 1이기 때문에, 이 값은 그 자릿수가 기여하는 실제 십진수 값에 직접적으로 영향을 줌.
            num = num * 2 + a[j]
        max_number = max(num, max_number)

        a[i] = 1 - a[i]

    print(max_number)

solution()