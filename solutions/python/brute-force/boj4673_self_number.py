# d(n) 함수 = 양의 정수 n에 대해서 n + 자리수합(n)을 처리하는 함수이다.
# 양의 정수 n이 주어졌을 때, 이 수를 시작으로 무한 수열을 만들 수 있다.
# ex) 33, 39, 51, 57 ...
#   => 위의 수열에서 앞의 수는 뒤의 생성자인데, 생성자가 없는 숫자의 경우도 있다.
#   => 이런 생성자가 없는 수를 셀프 넘버라고 한다. 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력한다.

# def chk_self_n(num):
#     # 셀프 넘버인지 확인하는 함수
#     # 확인해야 하는 범위 확인을 위해 자리수 확인
#     # N <= x + 9d => x >= N - 9d
#     is_self_num = False
#
#     d = len(str(num))
#     start = num - 9 * d if (num - 9 * d) >= 0 else 1
#
#     for chk_num in range(start, num):
#         n_list = sum(list(int(c) for c in str(chk_num)))
#         if chk_num + n_list == num:
#             is_self_num = True
#             break
#
#     return is_self_num
#
# for i in range(1, 10000):
#     if not chk_self_n(i):
#         print(i)

#-----------------------------------------------------------------------------------
# [방법2]
# 1부터 10,000까지 d(n) 함수에 넣는다고 가정
# => 2, 4, 6, 8, 10, 12, 14, 16, 18, 11, 13 .... 여기서 나오지 않는 수가 셀프 넘버
is_self_num = [False] * 10001

def d(num):
    return n + sum(map(int, str(n)))

for n in range(1, 10001):
    v = d(n)
    if v <= 10000:
        is_self_num[v] = True

for i in range(1, 10001):
    if not is_self_num[i]:
        print(i)


