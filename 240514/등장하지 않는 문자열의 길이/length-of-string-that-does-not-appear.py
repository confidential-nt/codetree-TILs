def solution():
    # 문제 해석에 유의.
    n = int(input())
    s = input()
    min_length = float("inf")
    check = [0] * (n + 1)
    for i in range(1, n+1):
        for j in range(n):
            sub_s = s[j:j+i]
            count = 0
            for k in range(n):
                if s[k:k+i] == sub_s:
                    count += 1
            if count >= 2:
                check[i] = 1
                break

        if not check[i]:
            min_length = min(i, min_length)    
        
    print(min_length)    

solution()