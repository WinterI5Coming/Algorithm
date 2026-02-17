T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())  # n = 보드 판 한 변 길이, m = 돌 놓는 횟ㅅ
    cmd = [tuple(map(int, input().split())) for _ in range(m)]

    # 보드 판 중앙을 먼저 채우고 시작
    # 1 = 흑, 2 = 백
    board = [[0 for _ in range(n)] for _ in range(n)]
    mid = n // 2
    board[mid - 1][mid - 1], board[mid][mid] = 2, 2
    board[mid - 1][mid], board[mid][mid - 1] = 1, 1

    # 돌을 놓았을 때 8방향으로 검사 진행
    # 특정 방향으로 쭉 검사할 때 근처에 나와 다른 색이 돌이 있는 방향만 검사
    # 해당 방향으로 나와 같은 색의 돌이 존재하는지 확인 후 있다면 뒤집는다.
    # => 해당 방향으로 0이 나오기 전까지 문자열을 가져온 후
    # => 나와 같은 색의 돌이 존재하는지 확인한다
    # EX. BWWWWBB / BWWWBWWB(해당 경우에서 뒤에 있는 BWWB는 안뒤집힌다. 처음 만난 같은 색 돌까지만)

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    for x, y, color in cmd:
        idx_x, idx_y = x - 1, y - 1
        board[idx_x][idx_y] = color
        opp_color = 1 if color == 2 else 2

        for d in range(8):
            nx = idx_x + dx[d]
            ny = idx_y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] != opp_color:
                # board 범위를 벗어나거나 인접칸에 상대 색이 아닌 경우 pass
                continue

            target = []
            while (0 <= nx < n and 0 <= ny < n) and board[nx][ny] == opp_color:
                # 범위 안에 있고 상대 색인 경우에만 해당 좌표들을 수집한다
                # => 범위를 벗어나거나 or 나와 같은 색을 만나거나 or 0을 만난 경우 멈추게 되어 있다
                # 그 중 나와 같은 색을 만나게 되었다면 nx, ny는 해당 칸의 좌표를 가르키게 된다
                target.append((nx, ny))
                nx += dx[d]
                ny += dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
                for tx, ty in target:
                    board[tx][ty] = color

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(f"#{test_case} {black} {white}")

    # if (0 <= nx < n and 0 <= ny < n) and board[nx][ny] == opp_color:
    #     target = []
    #     while (0 <= nx < n and 0 <= ny < n) and board[nx][ny] != 0:
    #         target.append(board[nx][ny])
    #         nx += dx[d]
    #         ny += dy[d]
    #
    #     t_idx = -1
    #     for i in range(len(target)):
    #         if target[i] == color:
    #             t_idx = i
    #             break
    #
    #     if t_idx != -1:
    #         for w in range(1, t_idx + 1):
    #             nx = idx_x + dx[d] * w
    #             ny = idx_y + dy[d] * w
    #             board[nx][ny] = color
    #
    # else:
    #     continue

    # print(board)
    # black = 0
    # white = 0
    # for row in board:
    #     black += row.count(1)
    #     white += row.count(2)
    #
    # print(f"#{test_case} {black} {white}")
