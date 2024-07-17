def solution():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    d = dict()
    for el in arr:
        if not el in d:
            d[el] = 0
        d[el] += 1
    sorted_result = sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True)
    for el in sorted_result[:k]:
        print(el[0], end=" ")


solution()