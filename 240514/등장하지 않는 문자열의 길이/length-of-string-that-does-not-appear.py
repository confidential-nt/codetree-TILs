def solution():
    n = int(input())
    s = input()
    min_length = float("inf")
    check = [0] * 101
    for i in range(n):
        for j in range(i+1,n+1):
            sub_s = s[i:j]
            length = j - i
            if check[length]:
                continue
            else:
                check[length] = 1    
            count = 0
            for k in range(n - length + 1):
                if s[k:k+length] == sub_s:
                    count += 1
            if count < 2:
                min_length = min(min_length, length)

    print(min_length)    

solution()