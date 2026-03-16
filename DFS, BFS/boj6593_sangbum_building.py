# from collections import deque
#
#
# def get_point(target):
#     global start_point
#     for z in range(L):
#         for x in range(R):
#             for y in range(C):
#                 if building[z][x][y] == target:
#                     return z, x, y
#
#
# """
# 상범 빌딩에서 탈출하는 가장 빠른 길은 무엇일까?
# 상범 빌딩은 각 변의 길이가 1인 정육면체로 이루어져 있으며,
#     비어있어서 지나갈 수 있거나(".") 금으로 이루어져 지나갈 수 없게("#") 되어있다.
# 인접한 6개의 칸으로 1분의 시간을 들여서 이동할 수 있고, 반드시 출구를 통해서만 탈출이 가능하다.
#
# 3차원으로 이뤄진 배열
# """
# while True:
#
#     L, R, C = map(int, input().split())  # L = 빌딩의 층 수, R, C = 한 층의 행과 열
#     if not (L and R and C):
#         break
#
#     building = []
#     for _ in range(L):
#         building.append([list(input()) for _ in range(R)])
#         input()
#
#     # start_point = [(z, x, y) for z in range(L) for x in range(R) for y in range(C) if building[z][x][y] == "S"]
#     # end_point = [(z, x, y) for z in range(L) for x in range(R) for y in range(C) if building[z][x][y] == "E"]
#     start_point, end_point = get_point("S"), get_point("E")
#
#     # 6방향 이동
#     dz = (-1, 1, 0, 0, 0, 0)
#     dx = (0, 0, -1, 1, 0, 0)
#     dy = (0, 0, 0, 0, -1, 1)
#     visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
#     visited[start_point[0]][start_point[1]][start_point[2]] = True
#     q = deque([(start_point, 0)])
#     best = 0
#     while q:
#         cur_pos, move = q.popleft()
#         for d in range(6):
#             nz, nx, ny = cur_pos[0] + dz[d], cur_pos[1] + dx[d], cur_pos[2] + dy[d]
#             if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
#                 if building[nz][nx][ny] == "E":
#                     best = move + 1
#                     q.clear()
#                     break
#                 if building[nz][nx][ny] == "." and not visited[nz][nx][ny]:
#                     visited[nz][nx][ny] = True
#                     q.append(((nz, nx, ny), move + 1))
#     # print(best)
#     if best == 0:
#         print("Trapped!")
#     else:
#         print(f"Escaped in {best} minute(s).")
#

# ----------------------------------------------------------------------------------------------
# [개선된 버전]
from collections import deque

dz = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dy = (0, 0, 0, 0, -1, 1)

while True:
    L, R, C = map(int, input().split())
    if not (L and R and C):
        break

    building = []
    start_point = None
    """
    building 배열을 만드는 것과 동시에 시작점을 찾을 수 있도록 수정
    """
    for z in range(L):
        floor = []
        for x in range(R):
            row = list(input())

            for y in range(C):
                if row[y] == "S":
                    start_point = (z, x, y)

            floor.append(row)
        building.append(floor)
        input()

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[start_point[0]][start_point[1]][start_point[2]] = True

    q = deque([(start_point[0], start_point[1], start_point[2], 0)])

    escaped = False
    best = 0
    while q:
        z, x, y, move = q.popleft()

        # q.clear()를 이용하는 것 보다는 해당 방향이 좀 더 자연스러운 BFS 활용이다.
        if building[z][x][y] == "E":
            escaped = True
            print(f"Escaped in {best} minute(s).")
            break

        for d in range(6):
            nz, nx, ny = z + dz[d], x + dx[d], y + dy[d]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                # 벽이 아닌 경우에만 통과하도록 조건을 수정했다.
                if building[nz][nx][ny] != "#" and not visited[nz][nx][ny]:
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, move + 1))

    if not escaped:
        print("Trapped!")
