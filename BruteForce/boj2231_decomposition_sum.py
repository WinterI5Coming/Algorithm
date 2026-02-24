N = int(input())

"""
분해합이란 주어진 자연수 N과 N을 이루는 각 자리수의 합을 의미한다
N의 가장 작은 생성자를 구하라는 의미는 
=> 어떤 자연수의 분해합이 N이 되는 수 중 가장 작은 수를 구하라는 것을 의미한다

1) 일단 분해합이 N이 되어야 하기 때문에 N보다 크거나 같은 것은 불가능 할 것이다.
2) N - (a + b + c) = 생성자
        각 자리수 합
"""
# target = N
# best = N
# while N > 0:
#
#     chk_num = N
#     n_list = list(int(c) for c in str(chk_num))
#
#     if chk_num + sum(n_list) == target:
#         best = min(best, chk_num)
#
#     N -= 1
#
# print(best if best != target else 0)

# -------------------------------------------------------------------------------
# [방법2]

"""
어떤 수 x의 분해합은 x + 자리수합(x)이다.

자리수합은 최대가 모든 자리가 9일 때니까
x가 d자리이면 자리수합 최대는 9d이다.

즉, x + 자리수합(x) = N이 되기 위해서는
x는 최소한 N - 9d 이상이어야 한다.

=> x + 자리수합(x) = N인데 여기서 자리수 합은 아무리 커도 9d를 넘기지 못한다
=> x + 자리수합(x) <= x + 9d
=> 해당 식을 정리하면, x + 9d >= N 이 되고, 결국 x >= N - 9d
=> 즉, 우리는 N - 9d부터 검사를 진행하면 된다.
"""

target = N
d = len(str(N))
start = max(1, N - 9 * d)

best = 0
for chk_num in range(start, target):
    n_list = list(int(c) for c in str(chk_num))

    if chk_num + sum(n_list) == target:
        best = chk_num
        break

print(best)