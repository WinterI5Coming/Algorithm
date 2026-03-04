T = int(input())

for test_case in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    edge = list(map(int, input().split()))

    """
    a, b 두 정점의 가장 가까운 공통 조상을 찾고,
    그 공통 조상을 루트로 하는 서브 트리의 크기를 출력한다.
    """


    def find_common_root(n1, n2, parents):

        # 8 -> 5 -> 3 -> 1
        # while True:
        #     # a, b의 조상에 대해서 set 에 하나씩 저장을 하면서 비교한다
        #     # 교집합이 나온순간 break
        #
        #     if n1 != 1:
        #         set1.add(parents[n1])
        #         n1 = parents[n1]
        #
        #     if n2 != 1:
        #         set2.add(parents[n2])
        #         n2 = parents[n2]
        #
        #     if set1 & set2:
        #         common = set1 & set2
        #         break
        set1 = set()
        common = None

        # n1에 대한 조상을 먼저 set 에 저장한다
        while n1 != 0:
            set1.add(n1)  # n1 자체가 n2의 조상일수도 있기 때문에 먼저 포함시킨다
            n1 = parents.get(n1, 0)

        # n2에 대한 조상을 거슬러 올라가면서, n1의 조상들과 교집합이 존재하는지 확인
        # 교집합이 존재하는 순간 그 조상이 바로 최소 거리의 공통조상이 된다
        while n2 != 0:
            pn2 = parents.get(n2, 0)
            if pn2 in set1:
                common = pn2
                break
            n2 = pn2

        return common


    def get_size(node):

        size = 0
        l, r = left.get(node, 0), right.get(node, 0)

        if l != 0:
            size += get_size(l)

        size += 1

        if r != 0:
            size += get_size(r)

        return size


    parent = {}
    left = {}
    right = {}
    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]

        parent[c] = p

        if p not in left:
            left[p], right[p] = 0, 0

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    common_root = find_common_root(a, b, parent)
    print(f"#{test_case} {common_root} {get_size(common_root)}")
