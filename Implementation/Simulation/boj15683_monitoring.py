"""
사무실에는 K 개의 CCTV 가 설치되어 있고, CCTV 는 5가지 종류가 존재한다.
CCTV 는 회전이 가능하고, 벽은 통과 불가능하다.

사각지대의 최소 크기 구한다.

=> 최대 4번까지 회전이 가능하다.
각 종류의 CCTV에 대해서 방향을 미리 정해놓는다.
"""

# [스택 + 상태복사]
# from collections import deque
#
# cctv_type = {
#     1: [[0], [1], [2], [3]],
#     2: [[0, 1], [2, 3]],
#     3: [[0, 3], [3, 1], [1, 2], [2, 0]],
#     4: [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
#     5: [[0, 1, 2, 3]]
# }
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# # cctv 위치, 방향 집
# cctvs = []
# for i in range(N):
#     for j in range(M):
#         if grid[i][j] != 0 and grid[i][j] != 6:
#             cctvs.append((i, j, grid[i][j]))
#
# board = [row[:] for row in grid]
# stack = deque([(0, board)])
# min_area = 10 ** 9
# while stack:
#     idx, b = stack.pop()
#
#     if idx == len(cctvs):
#         blank_area = 0
#         for i in range(N):
#             for j in range(M):
#                 if b[i][j] == 0:
#                     blank_area += 1
#
#         min_area = min(min_area, blank_area)
#         continue
#
#     x, y, type_ = cctvs[idx]
#     # 지금 선택한 cctv의 방향을 먼저 선택한다.
#     for directions in cctv_type[type_]:
#         for d in directions:
#             nx, ny = x + dx[d], y + dy[d]
#             while (0 <= nx < N and 0 <= ny < M) and b[nx][ny] != 6:
#                 # 벽이 아닌 경우에는 계속 진행한다.
#                 # b[nx][ny] == 0 으로 해버리면 => 다른 cctv를 만난 경우에도 멈춰버리기 때문에 주의
#                 if b[nx][ny] == 0:
#                     b[nx][ny] = -1
#
#                 new_b = [row[:] for row in b]
#                 stack.append((idx + 1, new_b))
#
# print(min_area)

# --------------------------------------------------------------------------------------------------
# [재귀 + 백트래킹]

cctv_type = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 3], [3, 1], [1, 2], [2, 0]],
    4: [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    5: [[0, 1, 2, 3]]
}

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cctv = [(i, j, grid[i][j]) for i in range(N) for j in range(M) if grid[i][j] != 6 and grid[i][j] != 0]
best = 10 ** 9


def watch(x, y, directions):
    changed = []

    for d in directions:
        nx, ny = x + dx[d], y + dy[d]
        while (0 <= nx < N and 0 <= ny < M) and grid[nx][ny] != 6:
            if grid[nx][ny] == 0:
                grid[nx][ny] = -1
                changed.append((nx, ny))
            nx, ny = nx + dx[d], ny + dy[d]

    return changed


def count_blank_area():
    blank_area = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                blank_area += 1

    return blank_area


def dfs(idx):
    global best

    if idx == len(cctv):
        best = min(best, count_blank_area())
        return

    x, y, type_ = cctv[idx]

    for directions in cctv_type[type_]:
        # 방문처리 하러간다.
        changed = watch(x, y, directions)
        dfs(idx + 1)
        for cx, cy in changed:
            grid[cx][cy] = 0


dfs(0)
print(best)
