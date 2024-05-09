def solution():
    tic_tac_toe = [[int(el) for el in input()] for _ in range(3)]
    is_already = [[[0] * 10 for _ in range(10)] for _ in range(10)]
    count = 0
    # 가로
    for i in range(3):
        a = tic_tac_toe[i][0]
        b = tic_tac_toe[i][1]
        c = tic_tac_toe[i][2]

        temp = sorted([a,b,c])
        ta,tb,tc = temp
        if is_already[ta][tb][tc]:
            continue

        if a == b and a != c:
            # print(a,b,c)
            count += 1
        elif a == c and a != b:
            # print(a,b,c)
            count += 1
        elif b == c and b != a:
            # print(a,b,c)
            count += 1  
        sorted_abc = sorted([a,b,c])
        sa,sb,sc = sorted_abc
        is_already[sa][sb][sc] = 1
    # 세로
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i == j == k):
                    a = tic_tac_toe[0][i]
                    b = tic_tac_toe[1][j]
                    c = tic_tac_toe[2][k]
                    temp = sorted([a,b,c])
                    ta,tb,tc = temp
                    if is_already[ta][tb][tc]:
                        continue

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
                    sorted_abc = sorted([a,b,c])
                    sa,sb,sc = sorted_abc
                    
                    is_already[sa][sb][sc] = 1

    # 대각선 오른쪽
    for i in range(3):
        for j in range(i+1, 3):
            for k in range(j + 1, 3):
                a = tic_tac_toe[0][i]
                b = tic_tac_toe[1][j]
                c = tic_tac_toe[2][k]
                temp = sorted([a,b,c])
                ta,tb,tc = temp
                if is_already[ta][tb][tc]:
                    continue

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
                sorted_abc = sorted([a,b,c])
                sa,sb,sc = sorted_abc
                is_already[sa][sb][sc] = 1

    # 대각선 왼쪽
    for i in range(2, -1, -1):
        for j in range(i - 1, -1, -1):
            for k in range(j - 1, -1, -1):
                a = tic_tac_toe[0][i]
                b = tic_tac_toe[1][j]
                c = tic_tac_toe[2][k]
                temp = sorted([a,b,c])
                ta,tb,tc = temp
                if is_already[ta][tb][tc]:
                    continue
                # print(a,b,c)
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
                sorted_abc = sorted([a,b,c])
                sa,sb,sc = sorted_abc
                is_already[sa][sb][sc] = 1

    print(count)
    
solution()