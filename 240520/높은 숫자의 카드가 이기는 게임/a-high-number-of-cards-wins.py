def solution():
    n = int(input())
    a = []
    b = [int(input()) for _ in range(n)]

    # in 연산 그냥 배열에서 하면 느림 -> set에서 함.
    b_set = set(b)
    for i in range(1, 2 * n + 1):
        if i not in b_set:
            a.append(i)

    # 둘 다 오름차순으로 정렬.
    a.sort()
    b.sort()
    
    count = 0
    b_index = 0
    for a_index in range(n):
        # b 카드의 작은 카드를 순서대로 마주치게 됨.
        # 왜 작은 카드부터? 큰 카드는 큰 카드끼리 붙어야 이길 가능성이 커지니까.
        # 현 시점 a 카드가 그 작은 카드보다 작다면 -> 가망 없음 -> 더 큰 카드를 찾아야 함. (그래야 최대한 많이 이기니까.)
        # b가 내는 순서가 정해져있긴 하지만, 어쨌든 이기는 조합을 구하는 거기 때문에 정렬해도 상관 없음.
        # 버리는 카드들은 자동으로 지는 매치에 들어가게 됨.
        if b_index < n and a[a_index] > b[b_index]:
            count += 1
            b_index += 1
    print(count)


solution()