# 선택된 2개의 값을 모두 고려하여 정렬 기준을 새롭게 설정하는 경우에는 python에서 lambda 함수만으로는 해결이 어렵기 때문에 꼭 custom comparator를 정의하여 해결해야 합니다. python3에서는 custom comparator를 만들고 sort함수의 key 인자로 넘길때 꼭, functools내 cmp_to_key 함수를 import하여 cmp_to_key(compare) 식으로 감싸줘야 합니다.

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