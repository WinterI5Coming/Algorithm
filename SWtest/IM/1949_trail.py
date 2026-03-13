# 등산로를 조성한다
# 등산로 조성을 위한 부지는 n*n 크기이고 최대한 넓은 긴 등산로를 만든다
# 각 숫자는 지형의 높이
# 조건)
# 1. 가장 높은 봉우리에서 시작해야 한다
# 2. 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결되어야 한다. => 대각선 불가
# 3. 딱 한 곳을 정해서 최대 k만큼 깎을 수 있다. (1 <= k <=5)

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]

    # 제일 높은 위치를 찾는다 (출발점)
    max_h = max(max(r) for r in ground)
    start_points = [(i, j) for i in range(n) for j in range(n) if ground[i][j] == max_h]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_trail = 0

    for sx, sy in start_points:
        # 시작점을 기준으로 방향을 순회한다
        # 스택을 이용하여 데이터들을 관리한다.
        # => [(위치, 높이, 깎기 사용 여부, 경로, 방문했던 곳)]

        init_case = [(sx, sy)]
        init_visit = {(sx, sy)}

        trail_stack = [(sx, sy, max_h, 0, init_case, init_visit)]

        while trail_stack:
            # stack이 모두 없어질 때 까지
            x, y, cur_h, is_cut, case, visit = trail_stack.pop()

            # 최대 길이 갱신
            if len(case) > max_trail:
                max_trail = len(case)

            # 현재 위치를 기준으로 4방향을 탐색한다
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 부지 범위를 벗어난 경우 제외
                if not (0 <= nx < n and 0 <= ny < n):
                    continue

                # 이미 방문한 경우
                if (nx, ny) in visit:
                    continue

                # 높이에 대해서 따져본다
                n_h = ground[nx][ny]

                if n_h < cur_h:
                    # 현재 높이보다 낮은 경우 => 바로 이동 가능
                    # case.append((nx, ny))를 하면 같은 주소를 공유하게 되기 때문에 불가
                    new_case = case + [(nx, ny)]
                    new_visit = visit | {(nx, ny)}

                    trail_stack.append((nx, ny, n_h, is_cut, new_case, new_visit))

                elif is_cut == 0:
                    # 현재 높이보다 높은 경우 => 깎기 사용 고려
                    # 다음 높이를 그 다음 경로까지 고려하여 현재 높이 보다 -1 만큼만 줄인다
                    # cur_h - 1 = n_h - k => k = n_h - cur_h + 1
                    need = n_h - cur_h + 1

                    if 1 <= need <= k:
                        # 깎아서 이동한 경우
                        new_case = case + [(nx, ny)]
                        new_visit = visit | {(nx, ny)}

                        trail_stack.append((nx, ny, cur_h - 1, 1, new_case, new_visit))

                # else: => 현재 높이보다 높은 경우 + 깎기도 불가

    print(f"#{test_case} {max_trail}")
