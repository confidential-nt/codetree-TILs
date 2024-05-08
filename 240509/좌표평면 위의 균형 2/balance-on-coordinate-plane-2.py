def solution():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    min_max_num = float("inf")

    for i in range(1, 101): # x축
        for j in range(1, 101): # y축
            if not (i % 2 == 0 and j % 2 == 0):
                # range(0, 101, 2) 이렇게 해버릴 수도 있음.
                continue
            nums = [0,0,0,0] # (x작,y크) (x작,y작) (x크,y작) (x크,y크)   
            for x,y in points:
                if x < i and y > j:
                    nums[0] += 1
                elif x < i and y < j:
                    nums[1] += 1
                elif x > i and y < j:
                    nums[2] += 1
                elif x > i and y > j:
                    nums[3] += 1
            max_num = max(nums)
            min_max_num = min(min_max_num, max_num)


    print(min_max_num)
solution()