def solution():
    N = int(input())
    s = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if s[i] == "C" and s[j] == "O" and s[k] == "W":
                    count += 1
    print(count)
solution()