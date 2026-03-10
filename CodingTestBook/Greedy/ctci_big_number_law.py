"""
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙을 의미한다.
단, 배열의 특정 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없다.
(서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다)

ex. [2, 4, 5, 4, 6], M = 8, K = 3일 때,
    6+6+6+5+6+6+6+5 = 46

=> 이전에 선택한 숫자와 현재 선택한 숫자의 idx가 같은지 다른지를 판단하여,
    연속해서 더할 수 있는 제한을 초기화할 건지를 판단한다.
"""
from sys import set_coroutine_origin_tracking_depth

# N, M, K = map(int, input().split())
# nums = sorted(list(map(int, input().split())), reverse=True)
# print(nums)
# # 일단 숫자 배열을 내림차순으로 정렬한다.
#
# best = 0
#
# current = 0
# limit = K
# while M > 0:
#
#     best += nums[current]
#     M -= 1
#
#     if current == 0:
#         # 덧셈을 진행할 때 마다 limit을 줄여나간다. => limit 이 0이 되면 current를 이동
#         limit -= 1
#     else:
#         current -= 1
#         continue
#
#     if limit == 0:
#         if current == 0:
#             current += 1
#         else:
#             current -= 1
#
#         limit = K
#
# print(best)

# --------------------------------------------------------------------------------
N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
print(nums)
# 일단 숫자 배열을 내림차순으로 정렬한다.

first = nums[0]
second = nums[1]

# 8(M)번 더해야 하고 3(K)번의 제한이 존재한다고 가정하면,
# => 사실상 가장 큰 수를 3번 연속해서 더하는 과정이 8 // 3 = 2 번 존재할 것이다.
# => 그 외에 2번은 두 번째로 큰 수를 더해주게 될 것이다.

best = 0
best += (M // K) * (first * K)
best += (M % K) * second

print(best)







