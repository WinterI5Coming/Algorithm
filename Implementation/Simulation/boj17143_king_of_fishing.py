R, C, M = map(int, input().split())

sharks = {}
for _ in range(M):
    r, c, speed, direction, size = map(int, input().split())
    sharks[(r - 1, c - 1)] = (speed, direction - 1, size)

shark_sum = 0
for c in range(C):

    # 상어 잡기
    for row in range(R):
        if (row, c) in sharks:
            shark_sum += sharks[(row, c)][2]
            del sharks[(row, c)]
            break

    new_sharks = {}
    # 상어 이동
    for (x, y), (s, d, z) in sharks.items():

        nx, ny, nd = x, y, d

        # 상하 이동
        if d <= 1:

            len_ = R - 1
            cycle = len_ * 2

            if d == 0:
                # 위로 이동
                t = cycle - x
            else:
                t = x

            nt = (t + (s % cycle)) % cycle

            nx = nt if nt <= len_ else cycle - nt
            nd = 1 if 1 <= nt <= len_ else 0

        # 좌우 이동
        else:

            len_ = C - 1
            cycle = len_ * 2

            if d == 2:
                # 오른쪽으로 이동
                t = y
            else:
                t = cycle - y

            nt = (t + (s % cycle)) % cycle

            ny = nt if nt <= len_ else cycle - nt
            nd = 2 if 1 <= nt <= len_ else 3

        # 이동 후 다른 상어 만난 경우
        if (nx, ny) not in new_sharks:
            new_sharks[(nx, ny)] = (s, nd, z)

        else:
            if z > new_sharks[(nx, ny)][2]:
                new_sharks[(nx, ny)] = (s, nd, z)

    sharks = new_sharks

print(shark_sum)

# ------------------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline
#
# R, C, M = map(int, input().split())
#
# # 0: 위, 1: 아래, 2: 오른쪽, 3: 왼쪽
# sharks = {}
#
# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     sharks[(r - 1, c - 1)] = (s, d - 1, z)
#
#
# def move_shark(r, c, s, d):
#     # 세로 이동
#     if d == 0 or d == 1:
#         if R == 1:
#             return 0, c, d
#
#         L = R - 1
#         cycle = 2 * L
#
#         # 방향이 아래면 +축, 위면 -축처럼 펼친 선분 위의 위치로 바꿈
#         if d == 1:   # 아래
#             t = r
#         else:        # 위
#             t = cycle - r
#
#         nt = (t + s) % cycle
#
#         nr = nt if nt <= L else cycle - nt
#         nd = 1 if 1 <= nt <= L else 0
#
#         return nr, c, nd
#
#     # 가로 이동
#     else:
#         if C == 1:
#             return r, 0, d
#
#         L = C - 1
#         cycle = 2 * L
#
#         if d == 2:   # 오른쪽
#             t = c
#         else:        # 왼쪽
#             t = cycle - c
#
#         nt = (t + s) % cycle
#
#         nc = nt if nt <= L else cycle - nt
#         nd = 2 if 1 <= nt <= L else 3
#
#         return r, nc, nd
#
#
# answer = 0
#
# for king_col in range(C):
#     # 1. 현재 열에서 가장 위 상어 잡기
#     for row in range(R):
#         if (row, king_col) in sharks:
#             answer += sharks[(row, king_col)][2]
#             del sharks[(row, king_col)]
#             break
#
#     # 2. 상어 이동
#     new_sharks = {}
#
#     for (r, c), (s, d, z) in sharks.items():
#         nr, nc, nd = move_shark(r, c, s, d)
#
#         if (nr, nc) not in new_sharks:
#             new_sharks[(nr, nc)] = (s, nd, z)
#         else:
#             # 큰 상어만 생존
#             if new_sharks[(nr, nc)][2] < z:
#                 new_sharks[(nr, nc)] = (s, nd, z)
#
#     sharks = new_sharks
#
# print(answer)

# ------------------------------------------------------------------------------------
# dir_rule = {0: 1, 1: 0, 2: 3, 3: 2}
# dx = (-1, 1, 0, 0)
# dy = (0, 0, 1, -1)
#
# R, C, M = map(int, input().split())  # R, C = 격자판 크기 / M = 상어의 수
# grid = [[0] * C for _ in range(R)]
# sharks = []
#
# for _ in range(M):
#     r, c, velocity, direction, size = map(int, input().split())
#     grid[r - 1][c - 1] = (r - 1, c - 1, velocity, direction - 1, size)
#     sharks.append((r - 1, c - 1, velocity, direction - 1, size))
#
# shark_sum = 0
# for c in range(C):
#     # 현재 위치 c열
#     # 현재 위치한 열에서 먼저 잡을 수 있는 상어를 확인한다.
#     for row in range(R):
#         if grid[row][c] != 0:
#             # 잡을 수 있는 상어를 찾은 경우
#             # => 잡은 상어의 무게 더해주기 + 잡은 상어 삭제
#             shark_info = grid[row][c]
#             shark_sum += shark_info[4]
#             grid[row][c] = 0
#             sharks.remove((shark_info[0], shark_info[1], shark_info[2], shark_info[3], shark_info[4]))
#             break
#
#     new_grid = [[0] * C for _ in range(R)]
#     new_sharks = []
#     # 잡은 이후에는 상어가 이동해야 한다.
#     for x, y, vel, dir_, size in sharks:
#
#         if dir_ <= 1:
#             move = vel % (2 * (R - 1)) if R > 1 else 0
#         else:
#             move = vel % (2 * (C - 1)) if C > 1 else 0
#
#         nx, ny = x, y
#         nd = dir_
#         for _ in range(move):
#             nx, ny = nx + dx[nd], ny + dy[nd]
#
#             if not (0 <= nx < R and 0 <= ny < C):
#                 nx, ny = nx - dx[nd], ny - dy[nd]
#                 nd = dir_rule[nd]
#                 nx, ny = nx + dx[nd], ny + dy[nd]
#
#         # 이동 이후에는 => 새로운 상어 리스트 갱신 + grid에서 상어 위치 데이터 갱신
#         # 이동이 완료되었다면
#         # => 다른 상어를 만났는지 아닌지를 확인한다.
#         if new_grid[nx][ny] != 0:
#             # 다른 상어를 만난 경우
#             # => 크기 비교 필요
#             other_shark = new_grid[nx][ny]
#
#             # 다른 상어의 크기가 더 작다면 => 새 상어로 덮어 씌어야 한다.
#             if size > other_shark[4]:
#                 new_sharks.remove(tuple(other_shark))
#                 new_grid[nx][ny] = (nx, ny, vel, nd, size)
#                 new_sharks.append((nx, ny, vel, nd, size))
#
#             # 새 상어의 크기가 더 작다면 => 해당 위치의 new_grid 는 그대로 놔둔다.
#         else:
#             # 다른 상어 만나지 않은 경우
#             new_grid[nx][ny] = (nx, ny, vel, nd, size)
#             new_sharks.append((nx, ny, vel, nd, size))
#
#     grid = new_grid
#     sharks = new_sharks
#
# print(shark_sum)

# """
# R * C 인 격자판에서 낚시왕이 낚시를 한다. 격자에는 최대 1마리의 상어가 있을 수도 있는데, 각 상어는 크기와 속도를 가진다.
# 처음에는 1번 열 한 칸 왼쪽에 있다가 1초마다 한칸씩 오른쪽 열로 이동한다.
#     낚시왕이 있는 열에서 땅과 제일 가까운 상어를 잡는다.
#     가장 오른쪽 열의 오른쪽 칸으로 이동하면 멈춘다.
#
# 그 동안 상어도 주어진 속도로 이동하게 된다.
#     격자판의 경계를 넘는 경우에는 방향을 반대로 바꾸어 계속 이동한다.
#     이동을 마친 후에 한 칸에 상어가 두 마리 이상 있는 경우 크키가 큰 상어가 나머지를 다 잡아 먹는다.
# """
# dir_rule = {0: 1, 1: 0, 2: 3, 3: 2}
# dx = (-1, 1, 0, 0)
# dy = (0, 0, 1, -1)
#
# R, C, M = map(int, input().split())  # R, C = 격자판 크기 / M = 상어의 수
# grid = [[0] * C for _ in range(R)]
#
# # 상어의 정보(r, c, 속력, 이동 방향, 크기)
# sharks = {}
# for shark_num in range(M):
#     r, c, velocity, direction, size = map(int, input().split())
#     grid[r - 1][c - 1] = shark_num + 1
#     sharks[shark_num + 1] = (r - 1, c - 1, velocity, direction - 1, size)
#
# best = 0
# for c in range(C):
#     # 현재 위치 c열
#
#     # 가장 큰 상어를 구한다.
#     catch_num = -1
#     catch = 0
#     for r in range(R):
#         if grid[r][c] != 0:
#             catch_num = grid[r][c]
#             best += sharks[grid[r][c]][4]
#             grid[r][c] = 0
#             del sharks[catch_num]
#             break
#
#     # 상어의 이동.
#     new_grid = [[0] * C for _ in range(R)]
#     new_sharks = {}
#     for shark_num, shark_info in sharks.items():
#         r, c, vel, d, size = shark_info
#         if grid[r][c] == 0:
#             continue
#
#         nr, nc = r, c
#         for _ in range(vel):
#             nr, nc = nr + dx[d], nc + dy[d]
#
#             # 벽 만난 경우
#             if not (0 <= nr < R and 0 <= nc < C):
#                 nr, nc = nr - dx[d], nc - dy[d]
#                 d = dir_rule[d]
#                 nr, nc = nr + dx[d], nc + dy[d]
#
#         if new_grid[nr][nc] == 0:
#             new_grid[nr][nc] = shark_num
#             new_sharks[shark_num] = (nr, nc, vel, d, size)
#
#         else:
#             other_num = new_grid[nr][nc]
#             other_size = new_sharks[other_num][4]
#
#             if size > other_size:
#                 del new_sharks[other_num]
#                 new_grid[nr][nc] = shark_num
#                 new_sharks[shark_num] = (nr, nc, vel, d, size)
#
#     grid = new_grid
#     sharks = new_sharks
#
# print(best)
