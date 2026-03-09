# from collections import deque
# from copy import deepcopy
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     """
#     N*N으로 이루어진 벌통에서 2명의 일꾼이 일을 한다.
#     각 일꾼은 가로로 연속이 되도록 M개의 벌통을 골라야 하고, 겹쳐서는 안된다.
#     고른 M개의 벌통에서 최대 채취할 수 있는 꿀은 C이며,
#         한 벌통에서 채취하는 꿀은 한 용기에만 담을 수 있고, 다른 벌통의 꿀과 같은 용기에 담을 수 없다.
#
#     수익은 한 벌통에서 채취한 꿀의 양을 x라고 했을 때 x*x가 되며,
#         두 일꾼이 벌어들일 수 있는 수익의 최대합을 구한다.
#
#     => 각 행에서 연속된 M개를 골랐을 때 최대가 되는 좌표 뽑는 함수?
#     """
#
#
#     def get_profit(honey_arr, limit):
#         sum_ = 0
#
#         for h in honey_arr:
#             if limit - h < 0:
#                 continue
#             sum_ += h * h
#             limit -= h
#
#         return sum_
#
#
#     N, M, C = map(int, input().split())
#     honey = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[False for _ in range(N)] for _ in range(N)]
#
#     stack = deque([(0, visited, 0)])
#     best = 0
#     while stack:
#         honey_sum, visit, cnt = stack.pop()
#
#         if cnt != 2:
#             for i in range(N):
#                 for j in range(N - M + 1):
#                     if all(not visit[i][j + m] for m in range(M)):
#
#                         target_honey = honey[i][j: j + M]
#
#                         n_visit = deepcopy(visit)
#                         for m in range(M):
#                             n_visit[i][j + m] = True
#
#                         stack.append((honey_sum + get_profit(target_honey, C), n_visit, cnt + 1))
#                         target_honey.sort(reverse=True)
#                         stack.append((honey_sum + get_profit(target_honey, C), n_visit, cnt + 1))
#
#         else:
#             # print(honey_sum, "!!!")
#             best = max(best, honey_sum)
#
#     print(f"#{test_case} {best}")

# ---------------------------------------------------------------------------------------------------
# [방법 2]
"""
벌통의 수익에 대해 먼저 계산을 끝내놓고 겹치지 않게 선택하도록 하는 방법으로 해결한다.
"""
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]


    # def get_max_profit(honey_arr):
    #
    #     stack = deque()
    #     for h in range(len(honey_arr)):
    #         # (선택한 idx, 합)
    #         stack.append((h, honey_arr[h], honey_arr[h] * honey_arr[h]))
    #
    #     max_ = 0
    #     while stack:
    #         prev_idx, limit, sum_ = stack.pop()
    #
    #         if limit <= C:
    #             max_ = max(max_, sum_)
    #
    #         for n_h in range(prev_idx + 1, len(honey_arr)):
    #             if limit + honey_arr[n_h] <= C:
    #                 stack.append((n_h, limit + honey_arr[n_h], sum_ + (honey_arr[n_h] * honey_arr[n_h])))
    #
    #     return max_

    # [비트마스크 버전]
    def get_max_profit_bitmask(honey_arr):

        max_ = 0

        for bit in range(1 << M):

            honey_sum = 0
            total_profit = 0
            for k in range(M):
                if bit & (1 << k):
                    honey_sum += honey_arr[k]
                    total_profit += honey_arr[k] ** 2

            if honey_sum <= C:
                max_ = max(max_, total_profit)

        return max_


    profit_grid = [[0 for _ in range(N - M + 1)] for _ in range(N)]
    # print(profit_grid)
    for i in range(N):
        for j in range(N - M + 1):
            # 해당 배열에 대한 부분집합을 구해서 그거에 대한 합 중 제일 큰 것을 찾아야 한다.
            target_honey = honey[i][j:j + M]
            # profit_grid[i][j] = get_max_profit(target_honey)
            profit_grid[i][j] = get_max_profit_bitmask(target_honey)


    # print(profit_grid)
    # profit_grid 에서 겹치지 않게 2개 뽑은 최대합 구한다.
    best = 0
    profit_stack = deque()
    for w1_r in range(N):
        for w1_c in range(N - M + 1):
            profit_stack.append(((w1_r, w1_c), profit_grid[w1_r][w1_c]))

    while profit_stack:
        worker_1, profit_sum = profit_stack.pop()

        for w2_r in range(N):
            for w2_c in range(N - M + 1):
                if (w2_r, w2_c) == worker_1:
                    continue

                if worker_1[0] == w2_r:
                    if worker_1[1] + M <= w2_c or w2_c + M <= worker_1[1]:
                        # 같은 행에 있는 걸 선택했다면 겹쳐서는 안된다.
                        # profit_grid 에서 같은 행에 있는 경우 M이상의 차이가 나야지 겹치지 않는것.
                        best = max(best, profit_sum + profit_grid[w2_r][w2_c])
                else:
                    best = max(best, profit_sum + profit_grid[w2_r][w2_c])

    print(f"#{test_case} {best}")

"""
1
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
"""
