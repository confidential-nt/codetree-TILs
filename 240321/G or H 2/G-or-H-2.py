def solution():
    N = int(input())
    if N == 1:
        print(0)
        return

    placed = [0] * 101
    for _ in range(N):
        coord, alpha = input().split()
        coord = int(coord)
        placed[coord] = alpha
    max_size = 0    
    for i in range(101):
        for j in range(i+1, 101):
            if placed[i] == 0:
                continue
            if placed[j] == 0:
                continue    
            arr = placed[i:j+1]

            num_of_g = 0
            num_of_h = 0
            for el in arr:
                if el == "G":
                    num_of_g += 1
                elif el == "H":
                    num_of_h += 1
            # 한쪽이 0 이면 다른 한쪽으로만 채워졌다는 이야기 -> is_all_same 구할 필요 x.    
            if num_of_g == 0 or num_of_h == 0 or num_of_g == num_of_h:
                max_size = max(max_size, j - i)   


    print(max_size)

solution()