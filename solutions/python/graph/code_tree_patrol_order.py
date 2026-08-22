n, k = map(int, input().split()) # n = 순찰 명령 길이, k = 접근 금지 구역 개수
patrol_cmd = input()
ban_spot = [list(map(int, input().split())) for _ in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cur_pos = [0, 0]

for cmd in patrol_cmd:
    # WASD 4개의 명령이 존재
    # 각 명령에 대해 해당 방향으로 이동 가능한지 먼저 판단 (값이 음수 or 30,000 초과)
    # 이동 가능하다면 해당 방향으로 이동
    # 그렇지 않다면 pass

    if cmd == "W":
        nx = cur_pos[0] + dx[0]
        ny = cur_pos[1] + dy[0]

    elif cmd == "A":
        nx = cur_pos[0] + dx[2]
        ny = cur_pos[1] + dy[2]

    elif cmd == "S":
        nx = cur_pos[0] + dx[1]
        ny = cur_pos[1] + dy[1]

    else:
        nx = cur_pos[0] + dx[3]
        ny = cur_pos[1] + dy[3]

    if not (0 <= nx <= 30_000 and 0 <= ny <= 30_000) or [nx, ny] in ban_spot:
        continue

    else:
        cur_pos[0] = nx
        cur_pos[1] = ny

print(*cur_pos)