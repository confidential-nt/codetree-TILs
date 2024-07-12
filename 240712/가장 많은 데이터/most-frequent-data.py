# 하지만 이 경우에는 각 문자열이 마치 배열의 index처럼 쓰이듯이 dict를 이용하여 (key, value) 형태로 각 문자열이 몇 번째 index에 있었는지를 저장해주면, 문자열 K가 주어졌을 때 O(1)만에 K가 몇 번째로 주어졌는지를 판단할 수 있습니다.

def solution():
    n = int(input())
    d = dict()
    for _ in range(n):
        key = input()
        if key not in d:
            d[key] = 0
        d[key] += 1
    
    print(max(d.values()))

solution()