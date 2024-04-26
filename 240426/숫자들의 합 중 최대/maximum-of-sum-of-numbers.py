def solution():
    X,Y = map(int, input().split())

    max_sum = 0
    for num in range(X,Y+1):
        max_sum = max(max_sum, digit_sum(num))
    print(max_sum)

def digit_sum(num):
    if num < 10:
        return num
    else:
        return digit_sum(num // 10) + num % 10 # 끝자리 제외한 나머지 부분 도려내기 + 끝부분만 도려내기
solution()