def post_order(node):
    if node == 0:
        return 0

    cnt = 1
    l = left.get(node, 0)
    r = right.get(node, 0)

    if l:
        cnt += post_order(l)

    if r:
        cnt += post_order(r)

    return cnt


T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선의 개수
    V = E + 1  # 정점의 수
    edge = list(map(int, input().split()))

    parent = {}  # 각 노드에 대한 부모 값을 저장
    # 각 부모에 대해 좌, 우 값 저장
    left = {}
    right = {}

    for i in range(E):
        # edge에서 2쌍씩 읽어들인다
        p, c = edge[i * 2], edge[i * 2 + 1]

        # 기본값(0) 설정
        if p not in left:
            left[p] = 0
            right[p] = 0

        # # 읽어들인 자식(c)값에 대해 부모 값이 존재하는지 확인
        # if parent.get(c, 0) == 0:
        #     parent[c] = p

        # 읽어들인 부모(p)값에 대해 좌, 우 값이 존재하는지 확인
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # print(parent)
    # print(left, right)
    print(f"#{test_case} {post_order(N)}")

"""
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
"""
