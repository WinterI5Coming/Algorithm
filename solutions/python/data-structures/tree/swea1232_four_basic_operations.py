# def post_order(node):
#     n_list = []
#     l, r = left[node], right[node]
#
#     if l != 0:
#         n_list.append(post_order(l))
#
#     if r != 0:
#         n_list.append(post_order(r))
#
#     # print(value[node])
#     if len(n_list) < 2:
#         n_list += [value[node]]
#
#     else:
#
#         operator = value[node]
#         b = n_list.pop()[0]
#         a = n_list.pop()[0]
#
#         if operator == "+":
#             n_list.append(a + b)
#         elif operator == "-":
#             n_list.append(a - b)
#         elif operator == "*":
#             n_list.append(a * b)
#         elif operator == "/":
#             n_list.append(int(a / b))
#
#     return n_list

def post_order(node):
    if left[node] == 0 and right[node] == 0:
        return value[node]

    a = post_order(left[node])
    b = post_order(right[node])
    op = value[node]

    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    return a // b

T = 1

for test_case in range(1, T + 1):
    N = int(input())  # N = 정점의 개수
    # E = N - 1  # 간선의 개수
    """
    정점이 정수면 => 정점 번호와 양의 정수가 주어진다.
    정점이 연산자면 => 정점 번호와 연산자, 해당 정점의 좌, 우 자식의 번호가 주어진다
    """

    value = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        info = input().split()
        p = int(info[0])

        if info[1].lstrip("-").isdecimal():  # 음수까지 안전하게 처리
            value[p] = int(info[1])

        else:
            value[p] = info[1]
            if len(info) >= 3:
                left[p] = int(info[2])
            if len(info) >= 4:
                right[p] = int(info[3])

    # print(value)
    # print(left, right)
    result = post_order(1)
    print(f"#{test_case} {result[0]}")

"""
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
"""
