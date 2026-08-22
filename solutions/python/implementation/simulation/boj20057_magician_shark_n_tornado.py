"""
N*N의 격자로 나누어진 모래밭이 존재하고, 각 좌표에는 해당 위치에 있는 모래의 양을 알려준다.
토네이도를 시전하면 격자의 가운데 칸부터 이동이 시작되며, 한 번에 한 칸만 이동할 수 있다.

한 칸 이동할 때 마다 모래는 일정한 비율로 흩날리게 된다.
    퍼지는 비율:
        - 1% : 진행 방향 기준 위쪽 앞 / 아래쪽 앞
        - 7% : 진행 방향 기준 바로 위 / 바로 아래
        - 2% : 진행 방향 기준 위쪽 두 칸 / 아래쪽 두 칸
        - 10%: 진행 방향 기준 대각선 앞 위 / 대각선 앞 아래
        - 5% : 진행 방향 기준 정면 두 칸 앞
        - alpha : 위의 퍼진 모래를 제외한 나머지 모래가 정면 한 칸 앞에 간다.

        즉 왼쪽 이동 기준으로 보면:

             2%
        10%  7%  1%
    5% alpha  y
        10%  7%  1%
             2%

    - 각 비율의 모래 양은 소수점 아래는 버린다.
    - alpha 위치에는 전체 모래에서 퍼진 모래 총합을 뺀 나머지가 간다.
    - 격자 밖으로 나간 모래는 격자에 쌓이지 않고, "밖으로 나간 모래 양"으로 누적한다.

1) 일단 먼저 중앙의 시작점을 구한 다음 거기서 출발한다.
2) 토네이도가 이동하는 것이 먼저
    2-1) 그 다음에 모래가 퍼지기 시작한다.
    2-2) 모레 확산 과정이 마무리 되었다면 방향 전환 + 해당 지점 모레 0 처리
"""

# [개선안]
from math import floor


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

# 기본 방향 좌측(0)을 기준으로 탐색해야 하는 것들을 미리 정리해 놓는다.
spread = [
    (-1, -1, 10),
    (-1, 0, 7),
    (-2, 0, 2),
    (-1, 1, 1),
    (1, 1, 1),
    (1, 0, 7),
    (2, 0, 2),
    (1, -1, 10),
    (0, -2, 5),
]


def rotate(a, b, d):
    for _ in range(d):
        a, b = -b, a
    return a, b


# 처음 시작점 구한다.
mid = N // 2
cur = (mid, mid, 0, 0, 0)  # (x, y, dir_, move_cnt, turn_cnr)

# 방향을 2번 바꿀 때 마다 move_limit을 +1씩 증가시켜 주어야 한다.
move_limit, turn_limit = 1, 2

out_sand = 0
while True:
    x, y, dir_, move_cnt, turn_cnt = cur

    # (0, 0)에 도착한 경우에는 종료
    if x == 0 and y == 0:
        break

    # 1) 토네이도가 현재 가지고 있는 방향을 한 칸 이동
    x, y = x + dx[dir_], y + dy[dir_]
    move_cnt += 1

    if grid[x][y] != 0:

        # 2) 이동한 좌표를 기준으로 주변으로 모래 확산 진행
        sand, total_divided_sand = grid[x][y], 0
        for move_x, move_y, percent in spread:
            rotate_x, rotate_y = rotate(move_x, move_y, dir_)
            divided_sand = sand * percent // 100
            total_divided_sand += divided_sand

            nx, ny = x + rotate_x, y + rotate_y
            # nx, ny가 범위 안쪽인 경우 => 해당 좌표에 모래 누적
            if 0 <= nx < N and 0 <= ny < N:
                grid[nx][ny] += divided_sand

            else:
                # 범위 바깥인 경우 => out_sand 에 누적
                out_sand += divided_sand

        # alpha 계산
        alpha = sand - total_divided_sand
        nx, ny = x + dx[dir_], y + dy[dir_]
        if 0 <= nx < N and 0 <= ny < N:
            grid[nx][ny] += alpha
        else:
            out_sand += alpha

    grid[x][y] = 0  # 기존 칸은 리셋
    # 3) 방향 전환
    if move_cnt == move_limit:
        move_cnt = 0

        dir_ = (dir_ + 1) % 4
        turn_cnt += 1
        if turn_cnt == turn_limit:
            move_limit += 1
            turn_cnt = 0
    cur = (x, y, dir_, move_cnt, turn_cnt)

print(out_sand)


# --------------------------------------------------------------------------------
# from math import floor


# N = int(input())
# grid = [list(map(int, input().split())) for _ in range(N)]

# dx = (0, 1, 0, -1)
# dy = (-1, 0, 1, 0)
# diagonal_rule = {
#     0: {"diagonal_x": (-1, 1, -1, 1), "diagonal_y": (-1, -1, 1, 1)},
#     1: {"diagonal_x": (1, 1, -1, -1), "diagonal_y": (-1, 1, -1, 1)},
#     2: {"diagonal_x": (-1, 1, -1, 1), "diagonal_y": (1, 1, -1, -1)},
#     3: {"diagonal_x": (-1, -1, 1, 1), "diagonal_y": (-1, 1, -1, 1)},
# }

# # 처음 시작하는 방향은 0(왼쪽), 다음 방향은 new_dir = (dir + 1) % 4 로 구할 것이다.
# # 토네이도처럼 도는 것은 방향 전환이 발생하는 2번째 타이밍에 이동해야 하는 칸 수를 +1 해준다. (처음 시작하는 기본 칸수 1)

# mid = N // 2
# cur = (mid, mid, 0, 0, 0)  # (x, y, dir, move, turn)
# move_cnt, turn_cnt = 1, 2

# sand_out_grid = 0
# while True:
#     x, y, dir_, move, turn = cur
#     if x == 0 and y == 0:
#         break

#     # 토네이도 이동
#     x, y = x + dx[dir_], y + dy[dir_]
#     move += 1

#     if grid[x][y] != 0:
#         # 모래 옮겨야 한다.
#         # 모레가 옮겨지는 기준 칸(y) 는 가지고 있는 방향으로 한 칸 이동한 칸
#         sand = grid[x][y]
#         divided = 0

#         grid[x][y] = 0
#         # 먼저 alpha를 제외한 부분을 본다.

#         # 1) 양 옆으로 두 칸씩 배분
#         for d in (1, -1):
#             new_dir = (dir_ + d) % 4

#             for m in range(1, 3):

#                 nx, ny = x + dx[new_dir] * m, y + dy[new_dir] * m

#                 if m == 1:
#                     divided_sand = floor(sand * 0.07)
#                 else:
#                     divided_sand = floor(sand * 0.02)

#                 divided += divided_sand
#                 if 0 <= nx < N and 0 <= ny < N:
#                     grid[nx][ny] += divided_sand
#                 else:
#                     sand_out_grid += divided_sand

#         # 2) 앞 뒤 대각
#         cur_diagonal = diagonal_rule[dir_]
#         for d in range(4):
#             nx, ny = (
#                 x + cur_diagonal["diagonal_x"][d],
#                 y + cur_diagonal["diagonal_y"][d],
#             )

#             if d <= 1:
#                 divided_sand = floor(sand * 0.1)
#             else:
#                 divided_sand = floor(sand * 0.01)

#             divided += divided_sand
#             if 0 <= nx < N and 0 <= ny < N:
#                 grid[nx][ny] += divided_sand
#             else:
#                 sand_out_grid += divided_sand

#         # 3) 두 칸 앞 쪽 + alpha
#         nx, ny = x + dx[dir_] * 2, y + dy[dir_] * 2
#         divided_sand = floor(sand * 0.05)
#         divided += divided_sand
#         if 0 <= nx < N and 0 <= ny < N:
#             grid[nx][ny] += divided_sand
#         else:
#             sand_out_grid += divided_sand

#         alpha = sand - divided
#         nx, ny = x + dx[dir_], y + dy[dir_]
#         if 0 <= nx < N and 0 <= ny < N:
#             grid[nx][ny] += alpha
#         else:
#             sand_out_grid += alpha

#     # 방향 전환
#     if move == move_cnt:
#         dir_ = (dir_ + 1) % 4
#         move = 0
#         turn += 1
#         if turn == turn_cnt:
#             move_cnt += 1
#             turn = 0
#     cur = (x, y, dir_, move, turn)

# print(sand_out_grid)
