# 관찰 해야 하는 것: 합들 중 최댓값이 최소가 되도록 하려면 가장 작은 수와 가장 큰 수를 순서대로 
# 매칭해주는 것이 유리하다는 것을 관찰해야함 <<< 절대로 못할듯;;;

def solution():
    n = int(input())
    answer = 0

    nums = []
    for _ in range(n):
        x,y = map(int, input().split())
        nums.append((y,x)) # 좀 더 간단하게 정렬할 수 있도록 y를 먼저, x를 나중에
    
    nums.sort() # y를 기준으로 정렬. 어차피 y는 다 다름.

    li, ri = 0, n -1 # 가장 작은 수, 가장 큰 수 각각의 인덱스
    while li <= ri:
        ly,lx = nums[li]
        ry,rx = nums[ri]

        answer = max(answer, ly + ry) # 최댓값 갱신

        # 묶음 처리 -> 이렇게 하는 이유: m개의 수들 각각을 묶음 처리해주려면 시간 오버.
        # n개의 다른 숫자들이 있다는 것을 이용하여 묶음 처리를 해줌.
        # 이렇게 하면 짝수개로 남김없이 매칭도 가능하고, 그 매칭한 것이 정답을 보장해주고..
        
        # 왼쪽 개수가 더 적다면
        # 왼쪽을 전부 매칭 시켜줌
        if lx < rx:
            # 오른쪽은 lx만큼 개수를 줄여줌.
            nums[ri] = (ry, rx - lx)
            # 왼쪽은 다 씀 -> 왼쪽 위치를 한 칸 뒤로 옮겨줌.
            li += 1

        elif lx > rx:
            nums[li] = (ly, lx - rx)
            ri -= 1
        
        # 개수가 동일하다면 양 쪽 다 씀
        # 둘다 인덱스 옮겨줌.
        else:
            li += 1
            ri -= 1
    print(answer)

solution()

# 2 5 8
# 2 3 3