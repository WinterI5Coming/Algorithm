def in_order(node):

    word = ""

    l = left[node]
    r = right[node]

    if l != "0":
        word += in_order(l)

    word += value[node]

    if r != "0":
        word += in_order(r)

    return word


T = 10

for test_case in range(1, T + 1):
    N = int(input())  # N = 정점의 수
    E = N - 1  # 간선의 수

    value = {}
    # parent = {}
    left = {}
    right = {}

    for i in range(N):
        info = list(input().split())
        # print(info)
        p, v, c = info[0], info[1], []
        if len(info) > 2:
            c = info[2:]

        value[p] = v

        if p not in left:
            left[p], right[p] = "0", "0"

        if c:
            for el in c:
                if left[p] == "0":
                    left[p] = el
                else:
                    right[p] = el

                # parent[el] = p

    # print(value)
    # print(parent)
    # print(left, right)
    result = in_order("1")
    print(f"#{test_case} {result}")




"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""
