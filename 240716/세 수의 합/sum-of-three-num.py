# # 같은 숫자 쌍이더라도, 고른 숫자의 위치가 다른 경우 다른 조합으로 생각해야함에 유의합니다.
# def solution():
#     n,k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     index_d = dict()

#     for i in range(n):
#         if arr[i] in index_d:
#             index_d[arr[i]].append(i)
#         else:
#             index_d[arr[i]] = [i]

#     d = dict()
#     visited = set()
#     count = 0

#     for i in range(n):
#         for j in range(i+1, n):
#             diff = k - (arr[i] + arr[j])
#             if diff in d:
#                 count += d[diff]
            
#             visited.add((i,j,))

#             if arr[i] in d:
#                 d[arr[i]] += 1
#             else:
#                 d[arr[i]] = 1

#             if arr[j] in d:
#                 d[arr[j]] += 1
#             else:
#                 d[arr[j]] = 1
        
#     print(count)

# solution()

def solution():
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

    ans = 0
    # 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
    for i in range(n):
        # 이미 순회한 적이 있는 숫자는 빼 버림으로서
        # 같은 조합이 여러번 세어지는 걸 방지합니다.
        count[arr[i]] -= 1

        for j in range(i):
            # 전처리를 해주었기 때문에 이미 순회한 적 있는 값은 hashmap에 없습니다.
            # 이와 같은 방식으로 같은 조합이 중복되어 세어지는 걸 방지할 수 있습니다.
            diff = k - arr[i] - arr[j]

            if diff in count:
                ans += count[diff]

    print(ans)

solution()