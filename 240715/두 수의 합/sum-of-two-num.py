# def solution():
#     n,k = map(int, input().split())
#     arr = list(map(int, input().split()))

#     d = dict()
#     for el in arr:
#         if el not in d:
#             d[el] = 0
#         d[el] += 1

#     count = 0
#     for el in arr:
#         target = k - el
#         if target in d and el in d:
#             if d[el] - d[target] == 0:
#                 if d[el] > 1:
#                     count += (d[el] * (d[target] - 1) // 2)
#                 elif d[el] == 1:
#                     count += 1
#                 if el == target:
#                     d.pop(el)
#                     continue
#                 d.pop(target)
#             elif d[el] - d[target] < 0:
#                 count += d[el] * d[target]
#                 d[target] = d[target] - d[el]
#                 d.pop(el)
#             elif d[el] - d[target] > 0:
#                 count += d[target] * d[el]
#                 d[el] = d[el] - d[target]
#                 d.pop(target)
#     print(count)


# solution()

def solution():
    # 변수 선언 및 입력:
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))

    count = dict()

    ans = 0
    # 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
    for elem in arr:
        diff = k - elem
        # 가능한 모든 쌍의 수를 세어줍니다.
        if diff in count:
            ans += count[diff]

        # 현재 숫자의 개수를 하나 증가시켜줍니다.
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1

    print(ans)