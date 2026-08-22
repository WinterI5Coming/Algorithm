"""
ATM 앞에 N명의 사람이 줄을 서있고, 사람들은 번호가 매겨져 있다.
각 사람이 돈을 인출하는데 걸리는 시간이 다르게 주어진다.

모든 사람이 돈을 인출하는데 걸리는 시간의 최솟값을 구한다.
"""

N = int(input())
withdraw_time = [0] + list(map(int, input().split()))
withdraw_time.sort()  # 1 2 3 3 4

sum_ = [0]
for i in range(1, N + 1):
    sum_.append(sum_[i - 1] + withdraw_time[i])
# print(sum_)
print(sum(sum_))