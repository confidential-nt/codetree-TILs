def solution():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    d = dict()
    for el in arr:
        if not el in d:
            d[el] = 0
        d[el] += 1
    sorted_result = sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True)
    for el in sorted_result[:k]:
        print(el[0], end=" ")


def solution2():
    # 변수 선언 및 입력:
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))

    count = dict()

    # 각 숫자가 몇 번씩 나왔는지를
    # hashmap에 기록해줍니다.
    for elem in arr:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1

    # hashmap을 순회하며
    # 중복되지 않게 새 배열을 만들어 줍니다.
    new_arr = [
        [value, key]
        for key, value in count.items()
    ]

    # 문제에서 요구한 정렬 기준에 맞추어 정렬합니다.
    new_arr = sorted(new_arr)

    # 출력:
    leng = len(new_arr)
    for i in range(leng - 1, leng - k - 1, -1):
        print(new_arr[i][1], end=" ")


solution()