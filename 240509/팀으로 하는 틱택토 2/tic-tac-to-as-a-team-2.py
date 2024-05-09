def solution():
    tic_tac_toe = [[int(el) for el in input()] for _ in range(3)]
    count = 0
    for i in range(3):
        a = tic_tac_toe[i][0]
        b = tic_tac_toe[i][1]
        c = tic_tac_toe[i][2]
        if a == b and a != c:
            # print(a,b,c)
            count += 1
        elif a == c and a != b:
            # print(a,b,c)
            count += 1
        elif b == c and b != a:
            # print(a,b,c)
            count += 1    

    for i in range(3):
        for j in range(3):
            if j - i < 0:
                continue
            if j - i > 1:
                continue
            for k in range(3):
                if (i == j == k) or (i != j and k > j):
                    a = tic_tac_toe[0][i]
                    b = tic_tac_toe[1][j]
                    c = tic_tac_toe[2][k]

                    # a,b 같/ a,c같 / b,c같/
                    if a == b and a != c:
                        # print(a,b,c)
                        count += 1
                    elif a == c and a != b:
                        # print(a,b,c)
                        count += 1
                    elif b == c and b != a:
                        # print(a,b,c)
                        count += 1    
    print(count)
    
solution()