def solution():
    n,k = map(int, input().split())
    changes = [tuple(map(int, input().split())) for _ in range(k)]
    arr = list(range(1,n + 1))
    count = {}
    for i in range(1, n + 1):
        if i not in count:
            count[i] = set({i})
    # 3k.
    for i in range(3 * k):
        index = i % k
        a,b = changes[index]

        count[arr[a - 1]].add(b)
        count[arr[b - 1]].add(a)

        
        temp = arr[a - 1]
        arr[a - 1] = arr[b - 1]
        arr[b - 1] = temp
        
    for item in count.values():
        print(len(item))

def solution2():
    # 입력:
    n, k = tuple(map(int, input().split()))
    change = [
        list(map(int, input().split()))
        for _ in range(k)
    ]

    # 변수 선언
    s = [set() for _ in range(n + 1)]
    ans = [0 for _ in range(n + 1)]

    # 시작 array를 arr에 표시합니다.
    arr = [i for i in range(n + 1)]

    for i in range(1, n + 1):
        # 각 i 숫자가 위치할 수 있는 자리를 HashSet에 넣어 저장합니다.
        s[i].add(i)
        ans[i] = 1

    # 3k번 자리를 바꿉니다.
    for _ in range(3):
        for (a, b) in change:
            # a와 b의 자리를 바꿔줍니다.
            # 이때 자리가 변화한 값은 arr[a]와 arr[b]밖에 없습니다.
            # 이 값들만 새로운 자리를 HashSet에 넣어 저장합니다.
            arr[a], arr[b] = arr[b], arr[a]

            if a not in s[arr[a]]:
                s[arr[a]].add(a)
                ans[arr[a]] += 1
            
            if b not in s[arr[b]]:
                s[arr[b]].add(b)
                ans[arr[b]] += 1

    # 3k번 자리를 바꾸면서 각 숫자들이 위치할 수 있는 값들의 개수를 ans 배열에서 확인합니다.
    for i in range(1, n + 1):
        print(ans[i])


solution2()

# 풀다보니.. count 하는 거에 중복제거 필요하겠더라 -> dict 대신 set