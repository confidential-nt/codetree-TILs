def solution():
    string = input()
    n = len(string)
    count = 0
    for i in range(n):
        if string[i] != "(":
            continue
        for j in range(i + 1, n):
            if string[j] == ")":
                count += 1
    print(count)

    

solution()