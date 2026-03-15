# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     """
#     집합 A가 있다.
#     집합 A의 부분집합 중 N개의 원소를 가지고 있고, 원소의 합이 K인 부분집합의 수를 출력한다.
#
#     """
#     N, K = map(int, input().split())
#     set_a = list(range(1, 13))
#
#     stack = deque()
#     stack.append((-1, 0, 0))
#
#     result = 0
#     while stack:
#         prev_idx, cnt, sum_ = stack.pop()
#
#         if cnt != N:
#             for i in range(prev_idx + 1, 12):
#
#                 stack.append((i, cnt + 1, sum_ + set_a[i]))
#
#         elif cnt == N and sum_ == K:
#             result += 1
#
#     print(f"#{test_case} {result}")

# -------------------------------------------------------------------
# [재귀]
# T = int(input())
#
# for test_case in range(1, T+1):
#     N,K = map(int, input().split())
#     set_a = list(range(1, 13))
#
#     result = 0
#
#     def get_subset(prev_idx, cnt, sum_):
#         global result
#
#         if sum_ > K:
#             return
#
#         if cnt != N:
#             for i in range(prev_idx + 1, 12):
#                 get_subset(i, cnt + 1, sum_ + set_a[i])
#
#         if cnt == N and sum_ == K:
#             result += 1
#             return
#
#     get_subset(-1, 0, 0)
#     print(f"#{test_case} {result}")

# -------------------------------------------------------------------
# [비트마스크]
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    set_a = list(range(1, 13))
    d = len(set_a)

    result = 0

    # 13개 원소를 가지고 있는 set_a의 모든 부분집합의 갯수를 (1 << d) 같이 표현한다
    for mask in range(1 << d):
        tmp = []
        for i in range(d):
            """
            여기서는 set_a에서 각 원소를 선택했는지를 확인하는 단계이다
            만약 mask가 5인 경우, 0101이 된다.
                => 1(0001) 의 경우 0101 & 0001 = 0001, 즉 0이 아니기 때문에 선택된 것으로 본다.
                => 2(0010) 의 경우 0101 & 0010 = 0000, 즉 0이기 때문에 선택되지 않은 것으로 본다.
                => 3(0011) 의 경우 0101 & 0011 = 0001, 즉 0이 아니기 때문에 선택된 것으로 본다. 
            """
            if mask & (1 << i):
                # 즉, 선택된 경우에는 추가한다.
                tmp.append(set_a[i])

        if len(tmp) == N and sum(tmp) == K:
            result += 1

    print(f"#{test_case} {result}")