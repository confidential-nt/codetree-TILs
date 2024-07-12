def solution():
    n = int(input())
    hashmap = dict()
    for _ in range(n):
        command = input().split()
        if command[0] == "add":
            hashmap[command[1]] = command[2]
        if command[0] == "find":
            if command[1] in hashmap:
                print(hashmap[command[1]])
            else:
                print(None)
        if command[0] == "remove":
            hashmap.pop(command[1])


solution()