"""
N*M 행렬의 맵이 존재한다. 0은 이동할 수 있는 곳, 1은 이동할 수 없는 벽을 의미한다.
(1,1)에서 출발해서 (N, M) 위치까지 최단 경로로 이동한다. (시작하는 칸과 끝나는 칸도 포함해서 센다.)

만약 이동하는 도중 한 개의 벽을 부수고 이동하는 것이 짧아진다면, 하나까지 부술 수 있다.
"""
from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

# 벽을 부술 수 있는지에 대한 상태 또한 가질 수 있어야 한다.
# visited[x][y][broken]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# (x, y, move, broke_wall)
q = deque([(0, 0, 1, 0)])

escaped = False
while q:
    x, y, move, broke_wall = q.popleft()

    if x == N - 1 and y == M - 1:
        escaped = True
        print(move)
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:

            # 0인 경우 => 그냥 이동
            if grid[nx][ny] == "0" and not visited[nx][ny][broke_wall]:
                visited[nx][ny][broke_wall] = True
                q.append((nx, ny, move + 1, broke_wall))

            # 1인 경우
            if grid[nx][ny] == "1" and broke_wall == 0 and not visited[nx][ny][1]:

                # => 벽을 부술 수 있으면 부순다.
                visited[nx][ny][1] = True
                q.append((nx, ny, move + 1, 1))

            else:
                # => 부술 수 없으면 이동 불가.
                continue

if not escaped:
    print(-1)

# -----------------------------------------------------------------------------------
"""
[이전 코드]

[반례]
2 4
0011
1010

해당 반례에서의 이전 코드 흐름은 다음과 같다:
    (0,0)에서 출발 할 때, 선택할 수 있는건 (0,1) 빈칸과 (1,0) 벽이 존재한다
        => (0, 1, 2, 0) 큐에 넣기
        => 벽을 부순 후 (1, 0, 2, 1) 큐에 넣기
        => 그런 다음에 visited[0][1] = True, visited[1][0] = True
    여기는 문제는 (1,1)에 도달할 때 발생한다.
        1. (0, 1, 2, 0)에서 (1, 1)로 가면 => 벽을 부수지 않은 상태로 도착한다.
        2. (1, 0, 2, 1)에서 (1, 1)로 가면 => 벽을 이미 부순 상태로 도착한다.

        이 두가지의 상태는 다른 상태여야만 한다.
            1번의 경우는 벽을 아직 한 번 더 부술 수 있지만, 2번의 경우는 더 이상 부술 수 없기 때문이다.
            그런데 visited[1][1] 하나만 사용하기 때문에 앞서 방문을 먼저 해버리면 나머지 경우를 다 막아버리게 된다.

=> 그러한 이유로 우리는 visited[x][y][broke_wall] 과 같이 벽을 부순 상태 또한 볼 수 있어야 한다.
"""
# from collections import deque
# from pprint import pprint
#
# N, M = map(int, input().split())
# grid = [list(input()) for _ in range(N)]
# pprint(grid)
# visited = [[False for _ in range(M)] for _ in range(N)]
# visited[0][0] = True
# # pprint(visited)
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# # (x, y, move, broke_wall)
# q = deque([(0, 0, 1, 0)])
#
# escaped = False
# while q:
#     x, y, move, broke_wall = q.popleft()
#
#     if x == N - 1 and y == M - 1:
#         escaped = True
#         print(move)
#         break
#
#     for d in range(4):
#         nx, ny = x + dx[d], y + dy[d]
#         if 0 <= nx < N and 0 <= ny < M:
#
#             # 0인 경우 => 그냥 이동
#             if grid[nx][ny] == "0" and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 q.append((nx, ny, move + 1, broke_wall))
#
#             # 1인 경우
#             if grid[nx][ny] == "1" and not visited[nx][ny]:
#                 if broke_wall == 0:
#                     # => 벽을 부술 수 있으면 부순다.
#
#                     grid[nx][ny] = "0"
#                     visited[nx][ny] = True
#                     q.append((nx, ny, move + 1, 1))
#
#                 else:
#                     # => 부술 수 없으면 이동 불가.
#                     continue
#
# if not escaped:
#     print(-1)
