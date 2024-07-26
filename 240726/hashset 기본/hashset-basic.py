def solution():
    n = int(input())
    commands = [input().split() for _ in range(n)]
    s = set()

    for do, value in commands:
        if do == "add":
            s.add(int(value))
        elif do == "remove":
            s.remove(int(value))
        else:
            print(str(int(value) in s).lower())
            
        


solution()