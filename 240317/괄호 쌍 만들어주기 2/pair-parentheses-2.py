def solution():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if j-i == 1 and l - k == 1 and s[i] == "(" and s[j] == "(" and s[k] == ")" and s[l] == ")":
                        
                        count += 1
    print(count)
    

solution()