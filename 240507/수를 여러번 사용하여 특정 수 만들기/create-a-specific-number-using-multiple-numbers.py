def solution():
    a,b,c = map(int, input().split())
    max_val = 0
    
    for i in range(c // a + 1):# 이렇게 해볼까 고민하긴 했었음..
        val = a * i
        last = c - val
        last_count = last // b
        val += b * last_count
        max_val = max(val, max_val)
        



    print(max_val)

solution()