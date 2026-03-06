# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#
#     INF = N * N * 10 + 1
#     dist = [[INF for _ in range(N)] for _ in range(N)]
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     dist[0][0] = grid[0][0]
#     stack = deque([((0, 0), grid[0][0])])
#     best = N * N * 10 + 1
#     while stack:
#         cur_pos, sum_ = stack.pop()
#
#         for d in range(4):
#             nx, ny = cur_pos[0] + dx[d], cur_pos[1] + dy[d]
#             if 0 <= nx < N and 0 <= ny < N:
#
#                 if dist[nx][ny] < sum_ + grid[nx][ny]:
#                     continue
#
#                 if nx == N - 1 and ny == N - 1:
#                     # 도착을 한 경우
#                     dist[nx][ny] = min(dist[nx][ny], sum_ + grid[nx][ny])
#                     continue
#
#                 dist[nx][ny] = min(dist[nx][ny], sum_ + grid[nx][ny])
#                 stack.append(((nx, ny), sum_ + grid[nx][ny]))
#
#     print(f"#{test_case} {dist[N-1][N-1]}")

# ================================================================================================
# [재귀]



# ================================================================================================
# [DP]

# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#
#     INF = float("inf")
#     dp = [[INF for _ in range(N)] for _ in range(N)]
#     dp[0][0] = grid[0][0]
#
#     """
#     해당 문제에서 오른쪽과 아래로만 이동할 수 있다는 조건이 존재했다.
#
#     따라서 특정 칸으로의 최소 이동 거리는 해당 칸의 위와 왼쪽과 위쪽 칸 중에서 최소거리에서 해당 칸의 값을 더한 것으로 볼 수 있다.
#     => a([i][j]) = min([i-1][j], [i][j-1]) + [i][j]
#     """
#
#     for i in range(N):
#         for j in range(N):
#             if i == 0 and j == 0:
#                 continue
#
#             best_prev = INF
#             if i > 0:
#                 best_prev = min(best_prev, dp[i - 1][j])
#             if j > 0:
#                 best_prev = min(best_prev, dp[i][j - 1])
#
#             dp[i][j] = best_prev + grid[i][j]
#
#     print(f"#{test_case} {dp[N - 1][N - 1]}")
