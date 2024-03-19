def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N): # 범위 선택 주의. j를 i + 1 부터 시작하게 하니까 틀림. 이유? 잘 모르겠음..뭔가 오류가 있나봄.
            avg = sum(arr[i:j+1]) / len(arr[i:j+1]) # 실수 나눗셈을 하지 않으면 자연수가 아닌 경우까지 포함됨.
            if avg in arr[i:j+1]:
                count += 1
    print(count)


solution()