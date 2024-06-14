import sys

# 두번째로 작은 수 === 가장 작은 수가 있고 그 다음으로 작다.
# 여러 개 있어도 -1
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    min_num = min(arr)
    value = float("inf")
    answer = -1
    for i in range(n):
        if arr[i] == min_num:
            continue
        if arr[i] == value:
            answer = -1
            continue
        if arr[i] < value:
            value = arr[i]
            answer = i + 1
    print(answer)    
solution()


# 정렬로 풀수도 있음
def solution2():

    # 변수 선언 및 입력
    n = int(input())
    a = list(map(int, input().split()))

    # 새로운 배열을 만들어 정렬하고
    # 2번째로 작은 숫자를 찾아냅니다.
    myarr = sorted(a)

    # isexist : 2번째로 작은 숫자가 존재하면 true
    isexist = False
    low2 = 0
    for elem in myarr:
        # 가장 처음으로 myarr[0]과 다른 숫자는
        # 2번째로 작은 숫자라고 할 수 있습니다.
        if elem != myarr[0]:
            low2 = elem
            isexist = True
            break

    # 2번째로 작은 숫자가 존재하지 않을 때
    if isexist == False:
        print(-1)
        sys.exit()

    ansidx = -1
    for idx, elem in enumerate(a):
        if elem == low2:
            # 2번째로 작은 숫자가 여러 개 있을 때
            if ansidx != -1:
                print(-1)
                sys.exit()

            ansidx = idx

    print(ansidx + 1)