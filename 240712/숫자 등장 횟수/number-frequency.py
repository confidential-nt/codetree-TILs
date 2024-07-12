# dict는 (key, value)형태로 데이터를 저장할 수 있고, key의 범위는 정의하기 나름이며 사용되는 메모리는 실제 dict에 들어간 데이터 수에 비례하므로, 숫자 범위와 무관하게 n개의 숫자에 대한 메모리만 사용하게 됩니다.
# (배열과는 다르게.)

def solution():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    question = list(map(int, input().split()))
    d = dict()
    for el in seq:
        if el not in d:
            d[el] = 0
        d[el] += 1
    
    for q in question:
        if q in d:
            print(d[q], end=" ")
        else:
            print(0)

solution()