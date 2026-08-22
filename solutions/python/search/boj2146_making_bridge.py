# """
# 먼저 grid를 읽어 들이면서 각 섬에 대한 파악을 먼저 진행한다.
# 과정에서 각각 섬에 대해서 다른 표시를 진행한다.
#     ex. 첫 번재 섬은 1로 표시, 두 번째 섬은 2로 표시 ...
#
# 각 섬의 외곽지역에서 출발한다.
#
# """
# from collections import deque
#
# N = int(input())
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# visited = [[False for _ in range(N)] for _ in range(N)]
# island_num = 1
#
# # 섬 라벨링
# for i in range(N):
#     for j in range(N):
#         if grid[i][j] == 1 and not visited[i][j]:
#
#             grid[i][j] = island_num
#             visited[i][j] = True
#             q = deque([(i, j)])
#
#             while q:
#                 x, y = q.popleft()
#
#                 for d in range(4):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if 0 <= nx < N and 0 <= ny < N:
#                         if grid[nx][ny] == 1 and not visited[nx][ny]:
#                             grid[nx][ny] = island_num
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
#
#             island_num += 1
#
#
# # 섬의 edge 찾기
# edge_point = [[] for _ in range(island_num)]
#
# for i in range(N):
#     for j in range(N):
#         if grid[i][j] != 0:
#
#             cur_island = grid[i][j]
#
#             for d in range(4):
#                 ni, nj = i + dx[d], j + dy[d]
#                 if (0 <= ni < N and 0 <= nj < N) and grid[ni][nj] == 0:
#                     edge_point[cur_island - 1].append((i, j, 0))
#                     break
#
#
# # 각 edge에서 BFS
# best = N ** 2
#
# for edge in edge_point:
#
#     visited = [[False] * N for _ in range(N)]
#     points = deque(edge)
#
#     for x, y, _ in edge:
#         visited[x][y] = True
#
#     while points:
#         ex, ey, move = points.popleft()
#
#         cur_island = grid[ex][ey]
#
#         for d in range(4):
#             nx, ny = ex + dx[d], ey + dy[d]
#
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#
#                 # 다른 섬 도착
#                 if grid[nx][ny] != 0 and grid[nx][ny] != cur_island:
#                     best = min(best, move)
#                     continue
#
#                 # 바다 확장
#                 if grid[nx][ny] == 0:
#                     visited[nx][ny] = True
#                     points.append((nx, ny, move + 1))
#
#
# print(best)
from collections import deque

# -------------------------------------------------------------------------------
# from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [[False for _ in range(N)] for _ in range(N)]
island_num = 1

# 섬 라벨링
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:

            grid[i][j] = island_num
            visited[i][j] = True
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            grid[nx][ny] = island_num
                            visited[nx][ny] = True
                            q.append((nx, ny))

            island_num += 1

best = N * N
while island_num > 0:

    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == island_num:

                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if (0 <= ni < N and 0 <= nj < N) and grid[ni][nj] == 0:
                        visited[i][j] = True
                        q.append((i, j, 0))
                        break

    while q:
        x, y, move = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] != island_num and not visited[nx][ny]:

                    if grid[nx][ny] != 0:
                        best = min(best, move)
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny, move + 1))

    island_num -= 1

print(best)

# -------------------------------------------------------------------------------
# [MultiSource BFS]
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

island = 1
visited = [[False] * N for _ in range(N)]

# 섬 라벨링
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:

            grid[i][j] = island
            visited[i][j] = True
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            grid[nx][ny] = island
                            visited[nx][ny] = True
                            q.append((nx, ny))

            island += 1

# Multi-source BFS
dist = [[-1] * N for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            q.append((i, j))
            dist[i][j] = 0

best = N * N

while q:
    x, y = q.popleft()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:

            if grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

            elif grid[nx][ny] != grid[x][y]:
                best = min(best, dist[nx][ny] + dist[x][y])

print(best)
