def solution():
    n,m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    # (무게, 가치)

    temp = [ (v/w, index) for index, (w,v) in enumerate(arr)]
    temp.sort(reverse=True)
    answer = 0
    for i in range(n):
        if m == 0:
            break

        if m - arr[temp[i][1]][0] >= 0:
            m -= arr[temp[i][1]][0]
            answer += arr[temp[i][1]][1]
        elif m != 0:
            answer += arr[temp[i][1]][1] * (m / arr[temp[i][1]][0])
            m = 0
    print( "{:.3f}".format(answer))        




solution()