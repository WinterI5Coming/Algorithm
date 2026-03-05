# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#
#     """
#     N명의 직원, N개의 일이 존재한다.
#     각 직원이 특정 일을 맡았을 때 성공할 수 있는 확률이 주어질 때,
#     주어진 일이 "모두" 성공할 확률의 최댓값을 구한다. (소수점 아래 7번째 자리에서 반올림해서 6번째까지 출력한다.)
#     """
#
#     # [(각 직원들이 맡은 일의 번호)]
#     stack = deque()
#     for i in range(N):
#         # 1번 직원 부터 고른다
#         visited = [False] * N
#         visited[i] = True
#
#         stack.append(([i], grid[0][i] / 100, visited))
#
#     best = 0.0
#     while stack:
#         selected, pct, v = stack.pop()
#         d = len(selected)
#
#         if pct <= best:
#             continue
#
#         if d != N:
#             for j in range(N):
#                 if v[j]:
#                     continue
#
#                 # selected + [j]에 대해서 합계 퍼센트 계산
#                 n_pct = pct * (grid[len(selected)][j] / 100)
#                 if n_pct <= best:
#                     continue
#
#                 n_v = v[:]
#                 n_v[j] = True
#                 stack.append((selected + [j], n_pct, n_v))
#
#         else:
#             if best < pct:
#                 best = pct
#
#     print(f"#{test_case} {best*100:.6f}")


# ---------------------------------------------------------------------------------------------
# [재귀]
# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#
#     # 미리 0.xx로 만들어 놓기
#     p = [[(el / 100) for el in row] for row in grid]
#
#
#     def dfs(idx, p_sum):
#         global best
#
#         if p_sum <= best:
#             return
#
#         if idx == N:
#             # 모든 직원이 일을 배분 받은 경우
#             best = max(best, p_sum)
#             return
#
#         for i in range(N):
#             # 일을 배분한다
#             if visited[i]:
#                 continue
#
#             visited[i] = True
#             dfs(idx + 1, p_sum * p[idx][i])
#             visited[i] = False  # 토글로 돌려놔야 한다
#
#
#     visited = [False] * N
#     # 0번째 직원부터 시작, 확률은 1부터시작
#     best = 0.0
#     dfs(0, 1)
#
#     print(f"#{test_case} {best * 100:.6f}")

# ---------------------------------------------------------------------------------------------
# [스택 + 비트마스크]
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 미리 0.xx로 만들어 놓기
    p = [[(el / 100) for el in row] for row in grid]

    best = 0.0
    stack = deque()
    # 현재 직원, 사용한 일, 확률 합
    stack.append((0, 0, 1))

    while stack:
        cur_person, mask, per_sum = stack.pop()

        if per_sum <= best:
            continue

        # 현재 직원 번호가 N이랑 같다면 끝
        if cur_person == N:
            best = per_sum

        # 작업 분배
        for i in range(N):
            if not mask & (1 << i):
                # 방문 하지 않은 일의 경우 => 분배
                # print(mask)
                # print(1 << i)
                # print(mask & 1 << i)
                stack.append((cur_person + 1, mask | (1 << i), per_sum * p[cur_person][i]))

    print(f"#{test_case} {best * 100:.6f}")
