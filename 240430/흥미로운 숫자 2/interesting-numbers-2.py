from collections import defaultdict

def solution():
    X,Y = map(int, input().split())
    answer = 0
    for num in range(X, Y + 1):
        nums_sep = [int(el) for el in str(num)]
        counter = defaultdict(int)
        for sep in nums_sep:
            counter[sep] += 1
        
        if len(counter.keys()) == 2 and 1 in counter.values():
            answer += 1
    print(answer)    
solution()