# 사람들에게 초대장을 나눠주려 하는데, 그룹 인원수가 k인 그룹에서 k−1명의 사람들이 초대장을 받았다면 나머지 한 사람도 무조건 초대장을 받아야합니다. 1번 사람에게는 무조건 초대장을 준다고 할 때, 확실하게 초대장을 받게 되는 인원 수를 구하는 프로그램을 작성하세요.

# 처음 주어진 사람별 속해있는 그룹정보를 인접리스트로 만들어 1번 사람을 시작으로 bfs 탐색 시작.
# 단 이때 queue에 새로운 원소를 추가하게 될 조건은, 현재 사람 x가 속해있는 그룹에서 x를 제거했을 때 
# 해당 그룹에 남아있는 사람의 수가 정확히 1명이 되는 경우.
# 이 경우 k명 중 정확하 k - 1명만 초대장을 받게 된 경우이므로 해당 사람을 queue에 넣어주는 식으로 진행하면 됨.
# 각 사람을 제거하고 확인하는데 효과적으로 이용할 수 있는 자료구조는 hashset -> hashset으로 그룹별로 초대받지 못한 사람 목록을 관리
# 그래프에서 노드의 수는 n, 간선의 수는 g이므로 시간복잡도는 o(n + g)

from collections import deque

# 변수 선언 및 입력:
n, g = tuple(map(int, input().split()))

invited = [False] * n
# 각 그룹마다 초대장을 받지 못한 사람들을 관리해줍니다.
groups = [set() for _ in range(g)]
# 각 사람이 어떤 그룹에 속하는지를 관리해줍니다.
people_groups = [[] for _ in range(n)]

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)

q.append(0)
invited[0] = True
while q:
    x = q.popleft()
    ans += 1

    # x가 들어있는 그룹에서 x를 지웁니다.
    # hashset에는 그룹에서 초대받지 않은 인원만을 남깁니다.
    for g_num in people_groups[x]:
        # 해당 그룹에서 x를 지웁니다.
        groups[g_num].remove(x)
        # 초대받지 않은 인원이 한명밖에 없다면 초대합니다.
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

# 초대장을 받는 인원을 출력합니다.
print(ans)