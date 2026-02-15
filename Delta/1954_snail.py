from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    snail_list = [[0 for _ in range(n)] for _ in range(n)]
    # pprint(snail_list)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dir_idx = 0
    pos = [0, 0]

    for i in range(n*n):
        # i + 1이 달팽이의 흔적
        # 현재 방향으로 이동할 수 있는지 확인 = 막혀있지 않은지 + 0 값이 맞는지
        # pos[0] + dr[dir_idx] / pos[1] + dc[dir_idx]

        snail_list[pos[0]][pos[1]] = i + 1

        # 방향 전환을 해야 하는 경우 = 막혀 있는 경우 or 다음 칸이 0이 아닌경우
        nr, nc = pos[0] + dr[dir_idx], pos[1] + dc[dir_idx]

        if not (0 <= nr < n and 0 <= nc < n) or snail_list[nr][nc] != 0:
            dir_idx = (dir_idx + 1) % 4

        pos[0] += dr[dir_idx]
        pos[1] += dc[dir_idx]


    # pprint(snail_list)
    print(f"#{test_case}")
    for row in snail_list:
        print(*row)