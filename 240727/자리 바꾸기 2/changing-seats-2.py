def solution():
    n,k = map(int, input().split())
    changes = [tuple(map(int, input().split())) for _ in range(k)]
    arr = list(range(1,6))
    count = {}
    for i in range(1,6):
        if i not in count:
            count[i] = set()
    # 3k.
    for i in range(3 * k):
        index = i % k
        a,b = changes[index]

        count[arr[a - 1]].add(b)
        count[arr[b - 1]].add(a)

        
        temp = arr[a - 1]
        arr[a - 1] = arr[b - 1]
        arr[b - 1] = temp
        
    for item in count.values():
        if len(item) == 0:
            print(1)
            continue
        print(len(item))


solution()