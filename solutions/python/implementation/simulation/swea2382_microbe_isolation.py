from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    dir_rule = {0: 1, 1: 0, 2: 3, 3: 2}
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque()
    for _ in range(K):
        x, y, cnt, direction = map(int, input().split())
        q.append((x, y, cnt, direction - 1))

    for _ in range(M):
        grid = [[0 for _ in range(N)] for _ in range(N)]

        while q:
            r, c, m_cnt, m_dir = q.popleft()

            nr, nc = r + dx[m_dir], c + dy[m_dir]

            # 경계에 도달한 경우
            if (nr == 0 or nr == N - 1) or (nc == 0 or nc == N - 1):
                if m_cnt // 2 != 0:
                    m_cnt //= 2
                    m_dir = dir_rule[m_dir]

                else:
                    # 약품에 닿아 군집이 0으로 사라지는 경우
                    continue

            if grid[nr][nc] == 0:
                # 그냥 이동하는 경우
                grid[nr][nc] = (m_cnt, m_cnt, m_dir)

            else:
                # 병합되는 경우
                old_cnt, total_cnt, old_dir = grid[nr][nc]

                if m_cnt > old_cnt:
                    grid[nr][nc] = (m_cnt, total_cnt + m_cnt, m_dir)

                else:
                    grid[nr][nc] = (old_cnt, total_cnt + m_cnt, old_dir)

        # 큐 재구성
        for i in range(N):
            for j in range(N):
                if grid[i][j] != 0:
                    _, total, dir_ = grid[i][j]
                    q.append((i, j, total, dir_))

    microbe_sum = sum(cnt for _, _, cnt, _ in q)
    print(f"#{test_case} {microbe_sum}")

# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M, K = map(int, input().split())  # N = 한 변의 길이, M = 격리 시간, K = 군집의 수
#
#     dir_rule = {0: 1, 1: 0, 2: 3, 3: 2}
#     dx = (-1, 1, 0, 0)
#     dy = (0, 0, -1, 1)
#
#     q = deque()
#     # 들어오는 input (세로 idx, 가로 idx, 미생물 수, 이동방향)
#     for _ in range(K):
#         x, y, microbe_cnt, direction = map(int, input().split())
#         q.append((x, y, microbe_cnt, direction - 1))
#
#     microbe_sum = 0
#     while M > 0:
#         n_grid = [[0 for _ in range(N)] for _ in range(N)]
#
#         for _ in range(len(q)):
#             r, c, m_cnt, m_dir = q.popleft()
#
#             nr, nc = r + dx[m_dir], c + dy[m_dir]
#             if 0 <= nr < N and 0 <= nc < N:
#                 # 범위 안에서 움직여야 한다.
#
#                 # 약품과 만난 경우 => 미생물 수 반감 + 방향 반대 전환
#                 if (nr == N - 1 or nr == 0) or (nc == N - 1 or nc == 0):
#                     if m_cnt // 2 != 0:
#                         n_grid[nr][nc] = (m_cnt // 2, m_cnt // 2, dir_rule[m_dir])
#                         q.append((nr, nc, m_cnt // 2, dir_rule[m_dir]))
#                     else:
#                         # 약품을 만나서 아예 사라져 버린 군집
#                         continue
#
#                 # 다른 군집과 만난 경우 => 만난 군집들의 미생물 수 합 + 미생물 수 많은 군집의 방향
#                 elif n_grid[nr][nc] != 0:
#                     existed = n_grid[nr][nc]  # (원래 존재하던 미생물 수, 미생물 수 합, 방향)
#                     q.remove((nr, nc, existed[1], existed[2]))  # 기존에 q에 들어있는 것들을 제거해줘야 한다.
#
#                     if existed[0] > m_cnt:
#                         # 기존에 있는 미생물 수가 더 많은 경우
#
#                         n_grid[nr][nc] = (existed[0], existed[1] + m_cnt, existed[2])
#                         q.append((nr, nc, existed[1] + m_cnt, existed[2]))
#
#                     else:
#                         # 새로 이동한 군집의 미생물 수가 더 많은 경우
#                         # n_dir = existed[3] if existed[2] > m_cnt else m_dir
#
#                         n_grid[nr][nc] = (m_cnt, existed[1] + m_cnt, m_dir)
#                         q.append((nr, nc, existed[1] + m_cnt, m_dir))
#
#                 # 그냥 이동하는 경우
#                 else:
#                     n_grid[nr][nc] = (m_cnt, m_cnt, m_dir)
#                     q.append((nr, nc, m_cnt, m_dir))
#
#         M -= 1
#         if M == 0:
#             while q:
#                 r, c, m_cnt, m_dir = q.popleft()
#                 microbe_sum += m_cnt
#
#     print(f"#{test_case} {microbe_sum}")
