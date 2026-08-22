T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N = 출석 번호 / M = 신청서 수
    apply = list(map(int, input().split()))

    parent = [i for i in range(0, N + 1)]

    # def find(x):
    #     if parent[x] != x:
    #         parent[x] = find(parent[x])
    #
    #     return parent[x]
    #
    #
    # def union(a, b):
    #     ra = find(a)
    #     rb = find(b)
    #
    #     if ra != rb:
    #         parent[rb] = ra

    # for i in range(M):
    #     a, b = apply[2 * i], apply[2 * i + 1]
    #     union(a, b)

    for m in range(M):
        a, b = apply[m * 2], apply[m * 2 + 1]

        # a의 루트 확인
        ra = a
        while parent[ra] != ra:
            ra = parent[ra]

        # b의 루트 확인
        rb = b
        while parent[rb] != rb:
            rb = parent[rb]

        if ra != rb:
            parent[rb] = ra

    print(parent)
    group_set = set()

    for i in range(1, N + 1):
        root = i
        while parent[root] != root:
            root = parent[root]
        group_set.add(root)

    print(f"#{test_case} {len(group_set)}")

"""
3
5 3
1 2 2 3 4 5
"""
