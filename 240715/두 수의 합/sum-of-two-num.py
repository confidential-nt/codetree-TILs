def solution():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))

    d = dict()
    for el in arr:
        if el not in d:
            d[el] = 0
        d[el] += 1

    count = 0
    for el in arr:
        target = k - el
        if target in d and el in d:
            # d[target] -= 1
            # d[el] -= 1
            # count += 1
            # if d[target] == 0:
            #     d.pop(target)
            # if d[el] == 0:
            #     d.pop(el)
            if d[el] - d[target] == 0:
                count += d[el]
                if el == target:
                    count *= 2
                    d.pop(el)
                    continue
                d.pop(target)
            elif d[el] - d[target] < 0:
                count += d[el]
                d[target] = d[target] - d[el]
                d.pop(el)
            elif dl[el] - d[target] > 0:
                count += d[target]
                d[el] = d[el] - d[target]
                d.pop(target)
    print(count)


solution()