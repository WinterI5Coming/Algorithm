"""
N 개의 섬을 연결하는 교통시스템 설계 프로그램을 진행한다.
모든 섬을 해저터널로 연결하는 것이 목표이다.
    두 섬을 선분으로 연결하고, 교차된다고 하더라도 물리적으로 연결되지 않을 것으로 가정한다.

단, 여기에는 환경 부담금 정책이 존재한다 : 환경 부담 세율(E)과 해저터널 길이(L)의 제곱의 곱 만큼 지불
                                            = E * L^2

환경 부담금 최소로 지불하고, 모든 섬을 연결할 수 있는 시스템을 설계한다.
"""

# import heapq
#
#
# def prim_mst(n, graph, start, tax_rate):
#     visited = [False] * n
#
#     total_cost = 0
#     edge_count = 0
#
#     heap = []
#     for weight, next_node in graph[start]:
#         heapq.heappush(heap, (weight, next_node))
#     visited[start] = True
#
#     while heap and edge_count < n - 1:
#         weight, node = heapq.heappop(heap)
#
#         if visited[node]:
#             continue
#
#         total_cost += tax_rate * float(weight)
#         edge_count += 1
#
#         visited[node] = True
#         for next_weight, next_node in graph[node]:
#             heapq.heappush(heap, (next_weight, next_node))
#
#     return total_cost
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n = int(input())
#     xs = list(map(int, input().split()))
#     ys = list(map(int, input().split()))
#     E = float(input())
#
#     graph = [[] for _ in range(n)]
#
#     for i in range(n):
#         x1, y1 = xs[i], ys[i]
#
#         for j in range(i + 1, n):
#             x2, y2 = xs[j], ys[j]
#
#             weight = (x2 - x1) ** 2 + (y2 - y1) ** 2
#
#             graph[i].append((weight, j))
#             graph[j].append((weight, i))
#
#     result = prim_mst(n, graph, 0, E)
#     print(f"#{test_case} {result:.0f}")

# ----------------------------------------------------------------------------------------------
# [Kruskal]
T = int(input())


def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ra, rb = find_root(parent, a), find_root(parent, b)

    if ra <= rb:
        parent[rb] = ra
    else:
        parent[ra] = rb


def kruskal_mst(n, edges, tax_rate):
    parent = [i for i in range(n)]

    total_cost = 0
    edge_cnt = 0

    for weight, a, b in edges:
        if find_root(parent, a) != find_root(parent, b):
            total_cost += tax_rate * float(weight)
            edge_cnt += 1

            union(parent, a, b)

        if edge_cnt == n - 1:
            break

    return total_cost


for test_case in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        x1, y1 = xs[i], ys[i]
        for j in range(i + 1, N):
            x2, y2 = xs[j], ys[j]

            weight = (x2 - x1) ** 2 + (y2 - y1) ** 2
            edges.append((weight, i, j))
    edges.sort(key=lambda x: x[0])

    print(f"#{test_case} {kruskal_mst(N, edges, E):.0f}")
