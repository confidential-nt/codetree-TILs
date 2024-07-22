# def solution():
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(4)]

#     ab_dict = dict()
#     a = arr[0]
#     b = arr[1]
#     for i in range(n):
#         for j in range(n):
#             key = a[i] + b[j]
#             if key not in ab_dict:
#                 ab_dict[key] = 0
#             ab_dict[key] += 1
       
#     cd_dict = dict()
#     c = arr[2]
#     d = arr[3]
#     for i in range(n):
#         for j in range(n):
#             key = c[i] + d[j]
#             if key not in cd_dict:
#                 cd_dict[key] = 0
#             cd_dict[key] += 1
    
    
#     count = 0
    
#     for ab_key, ab_val in ab_dict.items():
#         for cd_key, cd_val in cd_dict.items():
#             if ab_key + cd_key == 0:
#                 count += (ab_val * cd_val)
#     print(count)
# solution()

def solution():
    # 변수 선언 및 입력:
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    count = dict()

    ans = 0

    # A 수열에서 숫자 하나, B 수열에서 숫자 하나를 골랐을 때
    # 나올 수 있는 두 숫자의 합들을 hashmap에 기록해줍니다.
    for i in range(n):
        for j in range(n):
            sum_val = A[i] + B[j]
            if sum_val in count:
                count[sum_val] += 1
            else:
                count[sum_val] = 1

    # C, D 수열을 순회하며 쌍을 만들어줍니다.
    # 앞서 계산한 hashmap을 이용하면
    # C, D 수열에서 고른 값으로 A, B와 쌍을 만들 때
    # 총합이 0이 되는 쌍의 개수를 쉽게 구할 수 있습니다.
    for i in range(n):
        for j in range(n):
            diff = - C[i] - D[j]

            if diff in count:
                ans += count[diff]

    # 출력:
    print(ans)
solution()