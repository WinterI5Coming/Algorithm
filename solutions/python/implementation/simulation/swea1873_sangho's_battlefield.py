T = int(input())


def check_dir(value):
    if value == "^":
        return 0
    elif value == "v":
        return 1
    elif value == "<":
        return 2
    return 3


def move(move_cmd, x, y):
    if move_cmd == "U":
        return x - 1, y, 0, "^"
    elif move_cmd == "D":
        return x + 1, y, 1, "v"
    elif move_cmd == "L":
        return x, y - 1, 2, "<"
    return x, y + 1, 3, ">"


def shoot(x, y, dir_):
    nx, ny = x + dx[dir_], y + dy[dir_]

    while 0 <= nx < H and 0 <= ny < W:
        if grid[nx][ny] == "#":
            return
        if grid[nx][ny] == "*":
            grid[nx][ny] = "."
            return

        nx += dx[dir_]
        ny += dy[dir_]


for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    N = int(input())
    commands = input().strip()

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    cur_x, cur_y, cur_dir = 0, 0, 0

    for i in range(H):
        for j in range(W):
            if grid[i][j] in ("^", "v", "<", ">"):
                cur_x, cur_y = i, j
                cur_dir = check_dir(grid[i][j])

    for cmd in commands:
        if cmd != "S":
            nxt_x, nxt_y, nxt_dir, nxt_val = move(cmd, cur_x, cur_y)

            # 일단 방향은 무조건 바꿔야 함
            cur_dir = nxt_dir
            grid[cur_x][cur_y] = nxt_val

            # 그 다음 이동 가능하면 이동
            if 0 <= nxt_x < H and 0 <= nxt_y < W and grid[nxt_x][nxt_y] == ".":
                grid[cur_x][cur_y] = "."
                cur_x, cur_y = nxt_x, nxt_y
                grid[cur_x][cur_y] = nxt_val

        else:
            shoot(cur_x, cur_y, cur_dir)

    print(f"#{test_case}", end=" ")
    for row in grid:
        print("".join(row))