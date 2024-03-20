from itertools import permutations

def solution():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    
    count = 0
    for i in range(N):
        
        piece = A[i:i+M]
        if len(piece) != M:
            break
        
        is_beautiful = True
        for el in piece:
            if el not in B:
                is_beautiful = False
                break
        if is_beautiful:
            count +=1
    print(count)



solution()