from collections import deque
from pprint import pprint

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

virus = []
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            virus.append((grid[i][j], 0, i, j))
virus.sort(key=lambda a: a[0])

q = deque(virus)
while q:
    virus_type, time, x, y = q.popleft()

    if time == S:
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if (0 <= nx < N and 0 <= ny < N) and grid[nx][ny] == 0:
            grid[nx][ny] = virus_type
            q.append((grid[nx][ny], time + 1, nx, ny))

# pprint(grid)
print(grid[X - 1][Y - 1])

# ---------------------------------------------------------------------------------
# """
# 모든 바이러스는 1번부터 K 번까지의 바이러스 종류에 속한다.
# 1초마다 4방향(상하좌우)로 퍼져나가며, 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
# 또한 특정 칸에 이미 다른 바이러스가 존재한다면, 다른 바이러스는 들어갈 수 없다.
#
# S 초 후에(X, Y)에 있는 바이러스의 종류를 출력한다.
# """
# from collections import deque
# from pprint import pprint
#
# N, K = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
# S, X, Y = map(int, input().split())
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# virus_points = sorted([(i, j) for i in range(N) for j in range(N) if grid[i][j] != 0],
#                       key=lambda a: grid[a[0]][a[1]])
# q = deque(virus_points)
# while S > 0:
#     # q.append(virus_points)
#     len_ = len(q)
#     for _ in range(len_):
#         x, y = q.popleft()
#         virus_type = grid[x][y]
#
#         nx = x - 1
#         if 0 <= nx < N and grid[nx][y] == 0:
#             grid[nx][y] = virus_type
#             q.append((nx, y))
#
#         nx = x + 1
#         if 0 <= nx < N and grid[nx][y] == 0:
#             grid[nx][y] = virus_type
#             q.append((nx, y))
#
#         ny = y - 1
#         if 0 <= ny < N and grid[x][ny] == 0:
#             grid[x][ny] = virus_type
#             q.append((x, ny))
#
#         ny = y + 1
#         if 0 <= ny < N and grid[x][ny] == 0:
#             grid[x][ny] = virus_type
#             q.append((x, ny))
#
#     S -= 1
#
# # pprint(grid)
# print(grid[X - 1][Y - 1])
