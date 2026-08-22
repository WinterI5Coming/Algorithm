def cal_battery(route_list):
    total_b = 0

    for rx, ry in route_list:
        idx_x, idx_y = rx - 1, ry - 1
        total_b += battery_matrix[idx_x][idx_y]

    return total_b

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    battery_matrix = [list(map(int, input().split())) for _ in range(n)]

    # 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다
    # 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구한다
    # 1번은 사무실, 2~n번은 관리구역 번호를 의미한다.
    # 두 구역 간에 갈 때와 올 때의 배터리 소비량은 다를 수 있다

    # 처음 출발은 (1, i)로 반드시 출발한다
    # 그 다음 부터는 (i, j), (j, k)... 로 간다
    # 마지막은 (k, 1)로 끝난다

    visited = [False] * n
    stack = [([], visited)]
    min_bat = 99999
    while stack:
        route, visit = stack.pop()

        if not route:
            for i in range(2, n + 1):
                n_visit = visit[:]
                n_visit[0] = n_visit[i - 1] = True
                stack.append((route + [(1, i)], n_visit))

        elif len(route) < n:
            last_move = route[-1][1]
            if False not in visit:
                # 모든 곳을 다 방문하고 돌아가야 하는 경우
                stack.append((route + [(last_move, 1)], visit))

            else:
                for j in range(n):
                    if visit[j]:
                        continue
                    # last_move = route[-1][1]
                    n_visit = visit[:]
                    n_visit[j] = True
                    stack.append((route + [(last_move, j + 1)], n_visit))


        elif len(route) == n:
            # print(route)
            min_bat = min(min_bat, cal_battery(route))

    print(f"#{test_case} {min_bat}")