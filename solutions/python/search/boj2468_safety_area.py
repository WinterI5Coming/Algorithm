# """
# 어떤 지역의 높이를 파악하여, 그 지역에 비가 많이 내렸을 때 물에 잠기지 않는 안전한 영역이 최대 몇 개 만들어지는지 조사하고자 한다.
# 문제를 간단하게 하기 위해, 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
#
# 물에 잠기지 않은 영역이라 함은, 4방향으로 인접해 있는 영역들을 말한다.
#
# """
# from collections import deque
#
# N = int(input())
# area = [list(map(int, input().split())) for _ in range(N)]
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# # 지도에 존재하는 최소 높이와 최대 높이를 구한다.
# # 비가 오지 않는 경우 또한 고려해야 하기 때문에 0을 잊지 말 것.
# heights = [0] + list(set(area[i][j] for i in range(N) for j in range(N)))
# # print(heights)
#
# ground = [[0 for _ in range(N)] for _ in range(N)]
# max_area = 0
# for h in heights:
#
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if area[i][j] == h:
#                 ground[i][j] = 1
#
#     area_cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if ground[i][j] == 0 and not visited[i][j]:
#                 area_cnt += 1
#                 visited[i][j] = True
#                 q = deque([(i, j)])
#                 while q:
#                     x, y = q.popleft()
#
#                     for d in range(4):
#                         nx, ny = x + dx[d], y + dy[d]
#                         if 0 <= nx < N and 0 <= ny < N:
#                             if ground[nx][ny] == 0 and not visited[nx][ny]:
#
#                                 visited[nx][ny] = True
#                                 q.append((nx, ny))
#
#     max_area = max(max_area, area_cnt)
#
# print(max_area)
from collections import deque

# ----------------------------------------------------------------------
N = int(input())
area = [list(map(int ,input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

heights = sorted(set(h for row in area for h in row))
heights = [0] + heights

max_area = 0

for h in heights:

    visited = [[False] * N for _ in range(N)]
    area_cnt = 0

    for i in range(N):
        for j in range(N):

            if area[i][j] > h and not visited[i][j]:

                area_cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if area[nx][ny] > h and not visited[nx][ny]:
                                visited[nx][ny] =True
                                q.append((nx, ny))

    max_area = max(max_area, area_cnt)

print(max_area)