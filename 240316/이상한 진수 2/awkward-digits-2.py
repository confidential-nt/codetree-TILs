def solution():
    a = list(map(int, list(input())))
    length = len(a)

    max_number = 0
    for i in range(length):
        a[i] = 1 - a[i]

        num = 0
        for j in range(length):
            num = num * 2 + a[j]
        max_number = max(num, max_number)

        a[i] = 1 - a[i]

    print(max_number)

solution()