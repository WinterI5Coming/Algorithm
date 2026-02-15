T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    balloon_list = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    max_sum = 0
    for i in range(n):
        for j in range(m):
            # balloon_list[i][j]를 기준으로 합 계산
            sum_ = step = balloon_list[i][j]

            # 4 방향 순회하면서 합 계산
            for d in range(4):
                for st in range(1, step + 1):
                    # 해당 방향으로 step 만큼 갔을 때 => 벽에 막히지 않는지 검사
                    # balloon_list[i + dr[d]][j + dc[d]]
                    nr, nc = i + dr[d] * st, j + dc[d] * st
                    if 0 <= nr < n and 0 <= nc < m:
                        sum_ += balloon_list[nr][nc]
                    else:
                        # 범위 밖이라면 바로 탈출할 수 있도록
                        break

            max_sum = max(max_sum, sum_)

    print(f"#{test_case} {max_sum}")
