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
        
        for j in range(i): # 순회 범위에 유의. 이렇게 하면 중복 없이 모든 구간을 다 돌 수 있음.
            # 전처리를 해주었기 때문에 이미 순회한 적 있는 값은 hashmap에 없습니다.
            # 이와 같은 방식으로 같은 조합이 중복되어 세어지는 걸 방지할 수 있습니다.
            diff = k - arr[i] - arr[j]

            if diff in count:
                ans += count[diff]
    
    print(ans)

solution()

# 해설에서 k - arr[i] - arr[j]라는 수가 hashmap에 있는지를 확인하는 순간에 대해서 생각해보겠습니다.
# 코드 구조상 arr[0] ~ arr[i]까지의 수는 전부 hashmap에서 제거되어 있는 상황임을 유의해주세요.

# 즉, 고정된 i에 대해 (arr[i], arr[*], arr[*]) 형태로 세 수의 합이 k가 되는 서로 다른 가짓수를 중복없이 세고싶은 상황입니다. i는 고정되었고 j는 0 ~ i - 1 사이의 수로 하나씩 가정하게 됩니다.

# 그렇다면 모든 가능한 가짓수를 세어주기 위해 우리에게 필요한 형태가 (arr[i], arr[j], arr[s])라 했을 때, s는 i도 아닌, j도 아닌, 그러면서 arr[i] + arr[j] + arr[s] = k가 되어야만 합니다. 운이 좋게도 이 상황에 hashmap에는 arr[0] ~ arr[i]까지의 수가 전부 제거되어 있기에 그러한 s의 개수를 hashmap에서 바로 k - arr[i] - arr[j]을 조회하여 O(1)에 구할 수 있게 됩니다.

# 이렇게 계산했을 때 중복이 일어나지 않는 이유는 1) i가 고정되었을 때의 가짓수를 세고 있으며 2) j가 0부터 i - 1까지만 돌며 3) hashmap에는 arr[0] ~ arr[i]까지의 수가 전부 제거되어 있기에 j < i < s 를 만족하는 조합에 대해서만 가짓수로 판단하게 되기 때문입니다 :)