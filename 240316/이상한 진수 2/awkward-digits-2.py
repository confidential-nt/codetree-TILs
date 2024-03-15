def solution():
    a = [int(el) for el in input()]
    n = len(a)
    max_number = 0
    for i in range(n):
        if a[i] == 0:
            a[i] = 1
            max_number = max(max_number, get_number(a,n))
            a[i] = 0
        else:
            a[i] = 0
            max_number = max(max_number, get_number(a,n))
            a[i] = 1
    print(max_number)


def get_number(arr, n):
    result = 0
    for i in range(n):
        result += arr[i] * (2 ** (n - i- 1))
    return result






solution()