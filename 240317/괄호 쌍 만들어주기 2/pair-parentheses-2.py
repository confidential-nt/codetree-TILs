def solution():
    s = input()
    n = len(s)
    count = 0
    for i in range(n - 1):
        for j in range(i+1, n - 1):
          if s[i] == "(" and s[i + 1] == "(" and s[j] == ")" and s[j + 1] == ")":
            count += 1
    print(count)
    

solution()