def in_order(node):
    if node == 0:
        return ""

    return in_order(left[node]) + value[node] + in_order(right[node])

T = 10

for test_case in range(1, T+1):
    N = int(input())

    value = [""] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        info = input().split()
        p = int(info[0])
        value[p] = info[1]

        if len(info) >= 3:
            left[p] = int(info[2])
        if len(info) >= 4:
            right[p] = int(info[3])

    print(f"#{test_case} {in_order(1)}")