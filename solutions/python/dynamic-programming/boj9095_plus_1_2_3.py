"""
정수 N이 주어졌을 때,
N을 1,2,3의 합으로 나타내는 방법의 수를 구한다.
"""
from collections import deque

T = int(input())

for test_case in range(1, T+1):

    # N = int(input())
    #
    # stack = deque()
    # stack.append(([]))
    #
    # cnt = 0
    # while stack:
    #     n_list = stack.pop()
    #
    #     if sum(n_list) < N:
    #         for i in (1, 2, 3):
    #
    #             stack.append((n_list + [i]))
    #         continue
    #
    #     elif sum(n_list) == N:
    #         # print(n_list)
    #         cnt += 1
    #
    # print(cnt)

    """
    10이 주어진 경우,
        1을 표현하면 => 1가지
        2를 표현하면 => 2가지
            1+1, 2
        3을 표현하면 => 4가지
            1+1+1, 1+2, 2+1, 3
        4를 표현하면 => 7가지
            1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
        5를 표현하면 => 13가지
            1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+1+3, 1+3+1, 3+1+1,
             2+2+1, 2+1+2, 1+2+2, 3+2, 2+3
    
    즉, 점화식은 다음과 같다. a(n) = a(n-1) + a(n-2) + a(n-3)
    """

    N = int(input())

    dp = [0] * (N + 3)
    dp[1], dp[2], dp[3] = 1, 2, 4
    if N >= 4:
        for i in range(4, N + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])