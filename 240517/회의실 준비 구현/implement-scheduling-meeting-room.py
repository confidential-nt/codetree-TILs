def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    
    arr.sort(key=lambda x: x[1])
    result = [arr[0]]
    for i in range(1, n):
        a,b = result[-1]
        c,d = arr[i]
        if b <= c:
            result.append(arr[i])
    print(len(result))        

solution()