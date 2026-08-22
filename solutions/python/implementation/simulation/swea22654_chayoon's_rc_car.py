T = int(input())


def find_rc_car(grid):

    rc_car_x, rc_car_y = -1, -1
    fin_x, fin_y = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "X":
                rc_car_x, rc_car_y = i, j

            if grid[i][j] == "Y":
                fin_x, fin_y = i, j

    return rc_car_x, rc_car_y, fin_x, fin_y


def move_rc_car(cmd, x, y, dir_):

    if cmd == "A":
        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)

        nx, ny = x + dx[dir_], y + dy[dir_]
        if (0 <= nx < N and 0 <= ny < N) and grid[nx][ny] != "T":
            return nx, ny, dir_
        else:
            return x, y, dir_

    else:
        turn_rule = {"L": (dir_ - 1) % 4, "R": (dir_ + 1) % 4}

        dir_ = turn_rule[cmd]
        return x, y, dir_


for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    Q = int(input())

    str_x, str_y, fin_x, fin_y = find_rc_car(grid)
    str_dir = 0

    result = []
    # Q번 조종을 한다.
    for _ in range(Q):
        cmd_len, commands = input().split()
        cur_x, cur_y, cur_dir = str_x, str_y, str_dir

        for cmd in commands:
            cur_x, cur_y, cur_dir = move_rc_car(cmd, cur_x, cur_y, cur_dir)

        result.append(1 if cur_x == fin_x and cur_y == fin_y else 0)

    print(f"#{test_case} ", end="")
    print(*result)
