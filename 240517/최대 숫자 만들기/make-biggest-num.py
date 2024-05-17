from functools import cmp_to_key

def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    arr.sort(key=cmp_to_key(compare))

    print("".join([str(el) for el in arr]))

def compare(x,y):
    a = int(str(x) + str(y))
    b = int(str(y) + str(x))
    if a > b:
        return -1
    if b > a:
        return 1

    return 0        
    

solution()