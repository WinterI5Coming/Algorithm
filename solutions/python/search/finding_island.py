# from collections import deque
#
# N, M = map(int, input().split())
# grid = [list(map(int, input())) for _ in range(N)]
#
# dx = (-1, 1, 0, 0, -1, -1, 1, 1)
# dy = (0, 0, -1, 1, -1, 1, -1, 1)
#
# q = deque()
#
# cnt = 0
# for i in range(N):
#     for j in range(M):
#
#         if grid[i][j] == 1:
#
#             q.append((i, j))
#
#             while q:
#                 x, y = q.popleft()
#
#                 for d in range(8):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
#                         grid[nx][ny] = 0
#                         q.append((nx, ny))
#
#             cnt += 1
#
# print(cnt)

# -------------------------------------------------------------------------------------
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = (-1, 1, 0, 0, -1, -1, 1, 1)
dy = (0, 0, -1, 1, -1, 1, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        sx, sy = q.popleft()

        for d in range(8):
            nx, ny = sx + dx[d], sy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


island_cnt = 0
for i in range(N):
    for j in range(M):

        if grid[i][j] == 1 and not visited[i][j]:
            island_cnt += 1
            bfs(i, j)

print(island_cnt)
