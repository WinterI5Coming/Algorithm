# T = int(input())
#
# for test_case in range(1, T + 1):
#     """
#     0시부터 다음날 0시 이전까지 사용신청을 확인하여, 최대한 많은 화물차가 사용할 수 있도록 한다면
#     최대 몇 대의 화물차가 이용가능한가?
#
#     신청서에는 작업 시작 시간과 완료 시간이 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업 시작이 가능하다.
#     """
#
#     N = int(input())  # N = 신청서 수
#     works = [tuple(map(int, input().split())) for _ in range(N)]
#     # print(works)
#     works.sort(key=lambda x: (x[1], x[0]))  # 종료시간을 기준으로 우선적으로 정렬해야 유리하다.
#     # print(works)
#
#     now_ = 0
#     best = 0
#     for st, et in works:
#         if now_ <= st:
#             now_ = et
#             best += 1
#
#     print(f"#{test_case} {best}")

# --------------------------------------------------------------------------
# [DP]
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # N = 신청서 수
    works = [tuple(map(int, input().split())) for _ in range(N)]

    ends_at = [[] for _ in range(25)]
    for s, e in works:
        ends_at[e].append(s)

    dp = [0] * 25
    for t in range(1, 25):
        dp[t] = dp[t - 1]
        for s in ends_at[t]:
            dp[t] = max(dp[t], dp[s] + 1)
    # print(dp)

    print(f"#{test_case} {dp[24]}")
