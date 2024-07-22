def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]

    ab_dict = dict()
    a = arr[0]
    b = arr[1]
    for i in range(n):
        for j in range(n):
            key = a[i] + b[j]
            if key not in ab_dict:
                ab_dict[key] = 0
            ab_dict[key] += 1
       
    cd_dict = dict()
    c = arr[2]
    d = arr[3]
    for i in range(n):
        for j in range(n):
            key = c[i] + d[j]
            if key not in cd_dict:
                cd_dict[key] = 0
            cd_dict[key] += 1
    
    
    count = 0
    
    for ab_key, ab_val in ab_dict.items():
        for cd_key, cd_val in cd_dict.items():
            if ab_key + cd_key == 0:
                count += (ab_val * cd_val)
    print(count)
solution()