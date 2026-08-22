n, m = map(int, input().split())
l = int(input())
move_plan = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cur_pos = [0, 0]
is_success = True

for i in range(l):

    # 이동 계획을 하나씩 수행
    # 이동한 칸의 오염 수치만큼 정신력(100)을 감소
    # 다음 칸 이동계획 수행시 정신력이 음수가 되면 정지
    cmd = move_plan[i]

    if cmd == "U":
        nx = cur_pos[0] + dx[0]
        ny = cur_pos[1]

    elif cmd == "L":
        nx = cur_pos[0]
        ny = cur_pos[1] + dy[2]

    elif cmd == "R":
        nx = cur_pos[0]
        ny = cur_pos[1] + dy[3]

    else:
        nx = cur_pos[0] + dx[1]
        ny = cur_pos[1]

    if 0 <= nx < n and 0 <= ny < n:
        nm = grid[nx][ny]
        if m - nm > 0:
            # grid 범위를 벗어나지 않고 + 정신력이 음수가 아닌 경우 이동
            cur_pos[0], cur_pos[1] = nx, ny
            m -= nm

        else:
            # grid 범위를 벗어나지는 않지만 정신력이 음수가 되는 경우 stop
            is_success = False
            cur_pos[0], cur_pos[1] = nx, ny
            break

    else:
        # 이동 계획이 grid 범위를 벗어나는 경우 pass
        continue

print("Y" if is_success else "N")
print(cur_pos[0] + 1, cur_pos[1] + 1)





