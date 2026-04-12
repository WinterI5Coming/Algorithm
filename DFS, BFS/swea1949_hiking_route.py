from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_height = max(max(row) for row in grid)
    start_points = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == max_height]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    max_length = 0
    # 현재 위치(x, y), 현재 높이, 등산로 길이, 지형 깎기 사용 여부, 경로
    for x, y in start_points:

        stack = deque([(x, y, grid[x][y], 1, 0, {(x, y)})])
        while stack:
            cur_x, cur_y, cur_height, cur_length, did_cut, path = stack.pop()

            if max_length < cur_length:
                max_length = cur_length

            for d in range(4):
                nx, ny = cur_x + dx[d], cur_y + dy[d]
                if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in path:
                    continue
                # 범위 안에 있다

                nxt_height = grid[nx][ny]

                # 현재 높이 보다 낮다
                if nxt_height < cur_height:
                    stack.append((nx, ny, nxt_height, cur_length + 1, did_cut, path.union({(nx, ny)})))

                # 현재 높이 보다 높다면 => 갂기 사용?
                if nxt_height >= cur_height and not did_cut:
                    # cur_height - 1 = nxt_height - k
                    # k = nxt_height - cur_height + 1
                    need = nxt_height - cur_height + 1
                    if 1 <= need <= K:
                        stack.append((nx, ny, nxt_height - need, cur_length + 1, 1, path.union({(nx, ny)})))

    print(f"#{test_case} {max_length}")
