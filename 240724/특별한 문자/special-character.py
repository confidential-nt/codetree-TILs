def solution():
    string = input()
    d = dict()
    for s in string:
        if s not in d:
            d[s] = 0
        d[s] += 1
    
    finish = False
    for key, value in sorted(d.items(), key=lambda x: x[0]):
        if value == 1:
            print(key)
            finish = True
            break
    
    if not finish:
        print(None)

solution()