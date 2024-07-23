def solution():
    n = int(input())
    words = [input() for _ in range(n)]
    d = dict()
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in d:
            d[sorted_word] = 0
        d[sorted_word] += 1
    print(max(d.values()))
solution()