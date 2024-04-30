def solution():
    T,a,b = map(int, input().split())
    answer = 0
    # N = 1, S = 2
    arr = [0] * (b + 1)
    s = []
    n = []
    for _ in range(T):
        c,x = input().split()
        if c == "N":
            n.append(int(x))
        else:
            s.append(int(x))

    for k in range(a, b + 1):
        d1 = min([abs(k - el) for el in s]) # k로부터 가장 가까이 있는 S까지의 거리
        d2 = min([abs(k - el) for el in n]) # k로부터 가장 가까이 있는 N까지의 거리  

        if d1 <= d2:
            answer += 1
    print(answer)
solution()