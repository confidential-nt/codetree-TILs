def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N):
            sum_val = 0
            el_count = 0
            for k in range(i,j + 1):
                sum_val += arr[k]
                el_count += 1
            avg = sum_val / el_count
            exists = False
            for k in range(i,j+1):
                if avg == arr[k]:
                    exists = True
            if exists:
                count += 1        
    print(count)


solution()