def solution():
    n = int(input())
    candidates,scores = [],[]
    for _ in range(n):
        c,s = input().split()
        candidates.append(c)
        scores.append(int(s))

    a_score = 0
    b_score = 0
    a_win = False
    b_win = False
    count = 0
    for i in range(n):
        c = candidates[i]
        s = scores[i]

        if c == "A":
            a_score += s
        else:
            b_score += s

        if a_score > b_score:
            if not a_win:
                count += 1
                a_win = True
                b_win = False
        elif a_score < b_score:
            if not b_win:
                count += 1
                b_win = True
                a_win = False
        else:
            if (a_win and not b_win) or (not a_win and b_win):
                count += 1
                a_win = False
                b_win = False
    print(count)
 
solution()