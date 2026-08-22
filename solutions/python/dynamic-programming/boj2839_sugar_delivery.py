"""
정확하게 N킬로그램의 설탕을 배달해야 한다.
설탕은 봉지에 담겨져 있는데 3킬로 봉지와 5킬로 봉지가 존재한다.
최대한 적은 봉지를 가져 가야 한다.

ex. 18 = 5 * 3 + 3 * 1
"""

N = int(input())  # N 킬로그램의 설탕을 배달한다
INF = 10 ** 9
dp = [INF] * (N + 1)
dp[0] = 0

for x in range(1, N + 1):
    if x - 3 >= 0:
        dp[x] = min(dp[x], dp[x-3] + 1)

    if x - 5 >= 0:
        dp[x] = min(dp[x], dp[x-5] + 1)

# print(dp)
print(dp[N] if dp[N] != INF else -1)
