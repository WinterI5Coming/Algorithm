"""
"치킨 거리"라는 것은 집과 가장 가까운 치킨집 사이의 거리를 의미한다.
즉, 각각의 집은 치킨 거리를 가지고 있고, 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

"""

from collections import deque


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

chicken_store = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 2]
house = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]
min_chicken_dist = 10**9


def cal_chicken_move(stores):
    min_move_sum = 0

    for h in house:
        # 집을 하나 고른다. => 지금 선택한 치킨집 중에서 가장 가까운 거리를 구하기 위함
        min_move = 10**9
        for s in stores:
            chicken_distance = abs(s[0] - h[0]) + abs(s[1] - h[1])
            min_move = min(min_move, chicken_distance)

        min_move_sum += min_move

    return min_move_sum


def dfs(selected, idx):
    global min_chicken_dist

    if len(selected) == M:
        # 문제에서 최대 M개의 치킨집만 살려놓는다고 되어있었다.
        # => 그럼 최대 M개를 골랐을 때에만 계산하면 된다? 왜?
        # => 각 집의 입장에서는 선택지가 늘러난 것 뿐이기 때문에 최소 거리는 같거나 더 작아진다.
        # => 따라서 거리 계산을 매번 고를 때마다 해주는 것이 아니라 최대 M개를 골랐을 때 한 번만 해주면 된다.
        min_chicken_dist = min(min_chicken_dist, cal_chicken_move(selected))
        return

    for store_idx in range(idx + 1, len(chicken_store)):
        selected.append(chicken_store[store_idx])
        dfs(selected, store_idx)
        selected.pop()


dfs([], -1)
print(min_chicken_dist)

# ------------------------------------------------------------------------------------------------
# stack = deque([([], -1)])
# min_chicken_dist = 10**9

# while stack:
#     selected, idx = stack.pop()
#     if len(selected) == M:

#         min_chicken_dist = min(min_chicken_dist, cal_chicken_move(selected))
#         continue

#     for store_idx in range(idx + 1, len(chicken_store)):
#         n_selected = selected + [chicken_store[store_idx]]
#         stack.append((n_selected, store_idx))

# ------------------------------------------------------------------------------------------------
# # chicken_store에서 최대 M개로 이루어지는 조합의 수를 구해야 한다.
# stack = deque([([], -1)])  # ([선택한 치킨 집], idx, 치킨 거리 합)

# min_chicken_dist = 10**9
# while stack:
#     selected, idx = stack.pop()

#     if len(selected) < M:
#         for store_idx in range(idx + 1, len(chicken_store)):

#             selected.append(chicken_store[store_idx])
#             min_chicken_dist = min(min_chicken_dist, cal_chicken_move(selected))
#             selected.pop()

#             n_selected = selected + [chicken_store[store_idx]]
#             stack.append((n_selected, store_idx))
