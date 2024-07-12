def solution():
    n,m = map(int, input().split())
    d1 = dict()
    d2 = dict()
    for i in range(1, n+1):
        string = input()
        d1[i] = string
        d2[string] = i
    
    for _ in range(m):
        q = input()
        if q.isalpha():
            print(d2[q])
        else:
            print(d1[int(q)])


def solution2():
    # 이렇게 풀 수도 있음.
    # 변수 선언 및 입력:
    n, m = tuple(map(int, input().split()))

    # 다음과 같이 입력받으면 첫 번째 값이 0번 index에 저장된다는 점을 기억합시다.
    words = [
        input()
        for _ in range(n)
    ]

    string_to_num = dict()

    # 각 숫자의 대응되는 문자를 array에,
    # 각 문자의 대응되는 숫자를 hashmap에 기록해줍니다.
    for i in range(n):
        string_to_num[words[i]] = i + 1

    for _ in range(m):
        word = input()

        # 입력된 값이 숫자일 때에는 array에 저장한 문자를 출력합니다.
        # ord: 유니코드 얻기
        if ord(word[0]) >= ord('0') and ord(word[0]) <= ord('9'):
            num = int(word)
            # n번에 대응되는 문자열이 n-1번 index에 들어있기 때문에 1을 빼줍니다.
            print(words[num - 1])
        
        # 입력된 값이 문자일 때에는 hashmap에 기록된 대응되는 숫자를 출력합니다.
        else:
            print(string_to_num[word])

solution()