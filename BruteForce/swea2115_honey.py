from collections import deque
from copy import deepcopy

T = int(input())


def get_profit(t_honey):
    # 선택한 벌통에서 C를 넘지 않게 선택하되 최대 이익이 되어야 한다
    # => 조합

    max_ = 0
    d = len(t_honey)

    for mask in range(1 << d):

        honey_sum = 0
        honey_profit = 0
        for k in range(M):
            if mask & (1 << k):
                honey_sum += t_honey[k]
                honey_profit += t_honey[k] * t_honey[k]

        if honey_sum <= C:
            max_ = max(max_, honey_profit)

    return max_

    # sub_stack = deque()
    # # (선택한 idx, limit(C))
    # d = len(t_honey)
    # for i in range(d):
    #     sub_stack.append((i, t_honey[i] * t_honey[i], C - t_honey[i]))
    #
    # sum_ = 0
    # while sub_stack:
    #     prev_idx, profit, limit = sub_stack.pop()
    #
    #     sum_ = max(sum_, profit)
    #
    #     for j in range(prev_idx + 1, d):
    #         if limit - t_honey[j] >= 0:
    #             sub_stack.append((j, profit + t_honey[j] * t_honey[j], limit - t_honey[j]))
    #
    # return sum_


for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    stack = deque()
    # (총 수익, 방문, 직원)
    stack.append((0, visited, 0))
    best = 0
    while stack:
        total_profit, visit, worker_cnt = stack.pop()

        if worker_cnt != 2:
            for i in range(N):
                for j in range(N - M + 1):
                    # honey[i][j] ~ honey[i][j + M], range(M) 범위에서의 방문체크가 필요하다
                    not_visited = True
                    for m in range(M):
                        if visit[i][j + m]:
                            not_visited = False
                            break
                    if not_visited:
                        # 방문하지 않은 경우 = 통과
                        # => 수익 계산
                        n_visit = deepcopy(visit)
                        for m in range(M):
                            n_visit[i][j + m] = True

                        target = honey[i][j:j + M]
                        stack.append((total_profit + get_profit(target), n_visit, worker_cnt + 1))

        else:
            best = max(best, total_profit)

    print(f"#{test_case} {best}")

# ---------------------------------------------------------------------------------------------------
# [방법 2]
# """
# 벌통의 수익에 대해 먼저 계산을 끝내놓고 겹치지 않게 선택하도록 하는 방법으로 해결한다.
# """
# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M, C = map(int, input().split())
#     honey = [list(map(int, input().split())) for _ in range(N)]
#
#
#     # def get_max_profit(honey_arr):
#     #
#     #     stack = deque()
#     #     for h in range(len(honey_arr)):
#     #         # (선택한 idx, 합)
#     #         stack.append((h, honey_arr[h], honey_arr[h] * honey_arr[h]))
#     #
#     #     max_ = 0
#     #     while stack:
#     #         prev_idx, limit, sum_ = stack.pop()
#     #
#     #         if limit <= C:
#     #             max_ = max(max_, sum_)
#     #
#     #         for n_h in range(prev_idx + 1, len(honey_arr)):
#     #             if limit + honey_arr[n_h] <= C:
#     #                 stack.append((n_h, limit + honey_arr[n_h], sum_ + (honey_arr[n_h] * honey_arr[n_h])))
#     #
#     #     return max_
#
#     # [비트마스크 버전]
#     def get_max_profit_bitmask(honey_arr):
#
#         max_ = 0
#
#         for bit in range(1 << M):
#
#             honey_sum = 0
#             total_profit = 0
#             for k in range(M):
#                 if bit & (1 << k):
#                     honey_sum += honey_arr[k]
#                     total_profit += honey_arr[k] ** 2
#
#             if honey_sum <= C:
#                 max_ = max(max_, total_profit)
#
#         return max_
#
#
#     profit_grid = [[0 for _ in range(N - M + 1)] for _ in range(N)]
#     # print(profit_grid)
#     for i in range(N):
#         for j in range(N - M + 1):
#             # 해당 배열에 대한 부분집합을 구해서 그거에 대한 합 중 제일 큰 것을 찾아야 한다.
#             target_honey = honey[i][j:j + M]
#             # profit_grid[i][j] = get_max_profit(target_honey)
#             profit_grid[i][j] = get_max_profit_bitmask(target_honey)
#
#
#     # print(profit_grid)
#     # profit_grid 에서 겹치지 않게 2개 뽑은 최대합 구한다.
#     best = 0
#     profit_stack = deque()
#     for w1_r in range(N):
#         for w1_c in range(N - M + 1):
#             profit_stack.append(((w1_r, w1_c), profit_grid[w1_r][w1_c]))
#
#     while profit_stack:
#         worker_1, profit_sum = profit_stack.pop()
#
#         for w2_r in range(N):
#             for w2_c in range(N - M + 1):
#                 if (w2_r, w2_c) == worker_1:
#                     continue
#
#                 if worker_1[0] == w2_r:
#                     if worker_1[1] + M <= w2_c or w2_c + M <= worker_1[1]:
#                         # 같은 행에 있는 걸 선택했다면 겹쳐서는 안된다.
#                         # profit_grid 에서 같은 행에 있는 경우 M이상의 차이가 나야지 겹치지 않는것.
#                         best = max(best, profit_sum + profit_grid[w2_r][w2_c])
#                 else:
#                     best = max(best, profit_sum + profit_grid[w2_r][w2_c])
#
#     print(f"#{test_case} {best}")

"""
1
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
"""
