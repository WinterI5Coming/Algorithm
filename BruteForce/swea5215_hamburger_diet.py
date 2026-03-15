# from collections import deque
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     """
#     햄버거의 맛은 최대한 유지하면서 정해진 칼로리를 넘지 않아야 한다.
#     햄버거 재료에 대한 점수와 가게에서 재공하는 재료에 대한 칼로리가 주어질 때,
#     정해진 칼로리 이하의 조합 중 가장 점수가 높은(만족도가 높은) 햄버거를 조합한다.
#     (재료 중복 사용 불가)
#
#     """
#     N, L = map(int, input().split())
#
#     ingredients = []
#     for _ in range(N):
#         ingredients.append(tuple(map(int, input().split())))
#
#     # (선택한 idx, 점수, 칼로리)
#     stack = deque([(-1, 0, 0)])
#     best = 0
#     while stack:
#         select_idx, score, cal = stack.pop()
#
#         best = max(best, score)
#
#         for i in range(select_idx + 1, N):
#             selected_igd = ingredients[i]
#             if cal + selected_igd[1] <= L:
#                 stack.append((i, score + ingredients[i][0], cal + ingredients[i][1]))
#
#     print(f"#{test_case} {best}")

# -----------------------------------------------------------------------
# [비트마스크]
# T = int(input())
#
# for test_case in range(1, T+1):
#     N, L = map(int, input().split())
#     ingredients = [tuple(map(int, input().split())) for _ in range(N)]
#
#     best = 0
#     for mask in range(1 << N):
#
#         score = 0
#         cal = 0
#         for i in range(N):
#             if mask & (1 << i):
#                 score += ingredients[i][0]
#                 cal += ingredients[i][1]
#
#         if cal <= L:
#             best = max(best, score)
#
#     print(f"#{test_case} {best}")

# -----------------------------------------------------------------------
# [DP]
"""
DP로 문제를 풀 때 다음과 같이 정의한다.
dp[c] = 칼로리가 c일 때 얻을 수 있는 최대 점수
dp[c] = max(dp[c], dp[c - cal] + score) 단, c >= cal 일 때만 가능
"""
from _bisect import bisect_right

# T = int(input())
#
# for test_case in range(1, T+1):
#     N, L = map(int, input().split())
#     ingredients = [tuple(map(int, input().split())) for _ in range(N)]
#
#     dp = [0] * (L + 1)
#
#     for score, cal in ingredients:
#         for c in range(L, cal - 1, -1):
#             dp[c] = max(dp[c], dp[c - cal] + score)
#
#     print(f"#{test_case} {max(dp)}")

# -----------------------------------------------------------------------
# [Meet In The Middle]

from bisect import bisect_right


def get_subset(arr, d):
    """
    arr에 있는 재료들로 만들 수 있는 모든 부분집합을 생성한다.

    mask를 이용한 비트마스크 방식으로
    0 ~ (2^d - 1) 까지 순회하면서 부분집합을 만든다.

    각 부분집합에 대해
        cal  : 총 칼로리
        score: 총 맛 점수

    를 계산하고,
    칼로리가 제한 L 이하인 경우만 result에 저장한다.
    """

    result = []

    # 부분집합 개수는 2^d
    for mask in range(1 << d):

        score = 0
        cal = 0

        # mask의 각 비트를 확인하면서
        # 해당 재료를 선택할지 말지 결정한다.
        for i in range(d):

            # i번째 비트가 켜져 있으면
            # i번째 재료를 선택한 것이다.
            if mask & (1 << i):
                score += arr[i][0]  # 맛 점수
                cal += arr[i][1]    # 칼로리

        # 칼로리 제한 조건을 만족하는 경우만 저장
        if cal <= L:
            result.append((cal, score))

    return result


T = int(input())

for test_case in range(1, T + 1):

    # N : 재료 개수
    # L : 최대 허용 칼로리
    N, L = map(int, input().split())

    # (맛 점수, 칼로리)
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]

    """
    MITM 핵심 아이디어

    N개의 재료 전체에 대해 부분집합을 만들면

        2^N

    이 되어버린다.

    예를 들어
        N = 40

    이면

        2^40 ≈ 1조

    이라서 계산이 불가능하다.

    그래서 배열을 절반으로 나눈다.

        left  : N/2
        right : N/2

    그러면 각각

        2^(N/2)

    만 계산하면 된다.
    """

    mid = N // 2

    left_part = ingredients[:mid]
    right_part = ingredients[mid:]

    # 왼쪽 부분집합 생성
    left_list = get_subset(left_part, len(left_part))

    # 오른쪽 부분집합 생성
    right_list = get_subset(right_part, len(right_part))

    """
    right_list 형태

        (cal, score)

    예:

        (200, 30)
        (150, 20)
        (300, 40)
        ...
    """

    # 칼로리 기준 정렬
    right_list.sort()

    """
    prefix 최대값 배열 생성

    왜 필요한가?

    right_list는 cal 기준으로 정렬되어 있다.

    하지만 score는 정렬되어 있지 않다.

    예를 들어

    right_list

        cal   score
        100    10
        200    30
        250    20
        300    40

    만약 칼로리 제한이 260이면

        100, 200, 250

    까지 가능하다.

    그런데 score 최대값은

        30

    이다.

    그래서 prefix로
    "해당 위치까지의 최대 score" 를 미리 저장한다.
    """

    score_prefix = []

    best = 0

    for cal, score in right_list:

        # 지금까지 본 score 중 최대값 유지
        best = max(best, score)

        score_prefix.append(best)

    """
    right_list의 칼로리만 따로 뽑는다.

    이유:
    이분탐색을 하기 위해
    칼로리 배열이 필요하다.
    """

    right_cal_list = [x[0] for x in right_list]

    answer = 0

    """
    이제 left와 right를 조합한다.

    left 부분집합을 하나 고르고
    남은 칼로리에서 right 부분집합을 선택한다.
    """

    for cal, score in left_list:

        # 남은 칼로리
        remain = L - cal

        """
        remain 이하인 가장 큰 cal 찾기

        bisect_right는
        remain보다 큰 첫 위치를 반환한다.

        그래서 -1 하면
        remain 이하의 마지막 index가 된다.
        """

        idx = bisect_right(right_cal_list, remain) - 1

        # 가능한 조합이 있는 경우
        if idx >= 0:

            """
            score_prefix[idx] 는

            "idx까지 가능한 부분집합 중
             가장 높은 score"
            """

            answer = max(answer, score + score_prefix[idx])

    print(f"#{test_case} {answer}")