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
    for i in range(100):
        for j in range(i+1, 101):
            if placed[i] == 0:
                continue
            if placed[j] == 0:
                continue    
            arr = placed[i:j+1]
            is_all_same = True
            compare = arr[0]
            for el in arr[1:]:
                if el != compare:
                    is_all_same = False
                    break
                compare = el

            if is_all_same:
                max_size = max(max_size, j - i)
                continue

            num_of_g = 0
            num_of_h = 0
            for el in arr:
                if el == "G":
                    num_of_g += 1
                elif el == "H":
                    num_of_h += 1
            if num_of_g == num_of_h:
                max_size = max(max_size, j - i)   


    print(max_size)

solution()