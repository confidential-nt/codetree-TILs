def solution():
    n = int(input())
    s = input()
    min_length = float("inf")
    for i in range(n):
        for j in range(i+1,n+1):
            sub_s = s[i:j]
            length = j - i
            count = 0
            for k in range(n - length + 1):
                if s[k:k+length] == sub_s:
                    count += 1
            if count < 2:
                # print(sub_s, length)
                min_length = min(min_length, length)
                break
        if min_length != float("inf"):
            break
    print(min_length)    

solution()