def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N): # 범위 선택 주의. j를 i + 1 부터 시작하게 하니까 틀림. 출력해보니까 i=0일때 j가 i면 0~99 / i + 1이면 1~99인데 이래서 틀리는 것 같음. 후자의 경우, 슬라이싱을 할 때 arr[i:j]를 하게 되는데, 이러면 배열의 원소를 옳게 슬라이싱 못함.
            avg = sum(arr[i:j+1]) / len(arr[i:j+1]) # 실수 나눗셈을 하지 않으면 자연수가 아닌 경우까지 포함됨.
            if avg in arr[i:j+1]:
                count += 1
    print(count)


solution()