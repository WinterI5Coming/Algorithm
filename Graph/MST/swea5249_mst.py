"""
0 ~ V 번까지의 노드와 E개의 간선을 가진 그래프의 정보가 주어질 때,
    최소신장트리를 구성하는 간선의 가중치 모두 더해 출력한다.
"""

# # [Prim]
import heapq

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    # Prim에서는 인접리스트를 활용한다.
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())

        # (start, end, weight)
        adj_list[n1].append((n1, n2, w))
        adj_list[n2].append((n2, n1, w))


    def prim_mst(v, adj_list, start):

        visited = [False] * (v + 1)
        edge_cost = 0
        edge_cnt = 0

        priority_q = []
        # 시작 노드(start)가 선택할 수 있는 것들을 먼저 넣는다.
        for _, e, w in adj_list[start]:
            heapq.heappush(priority_q, (w, e))
        visited[start] = True

        while priority_q and edge_cnt < v:
            weight, end = heapq.heappop(priority_q)

            if visited[end]:
                continue

            edge_cost += weight
            edge_cnt += 1
            visited[end] = True

            for _, e, w in adj_list[end]:
                heapq.heappush(priority_q, (w, e))

        return edge_cost


    print(f"#{test_case} {prim_mst(V, adj_list, 0)}")

# ---------------------------------------------------------------------------------------
# [Kruskal]
T = int(input())

for test_case in range(1, T + 1):

    def find_root(parent, x):
        root = x
        if parent[x] != root:
            root = find_root(parent, parent[x])

        return root


    def union(a, b, parent):
        root_a, root_b = find_root(parent, a), find_root(parent, b)

        if root_a <= root_b:
            parent[b] = root_a
        else:
            parent[a] = root_b


    def kruskal_mst(v, edges):

        parent = [i for i in range(v + 1)]

        edge_cost = 0
        edge_cnt = 0

        for w, start, end in edges:

            if find_root(parent, start) != find_root(parent, end):
                # root_a, root_b = find_root(parent, start), find_root(parent, end)
                union(start, end, parent)

                edge_cost += w
                edge_cnt += 1

                if edge_cnt == v:
                    return edge_cost


    V, E = map(int, input().split())

    # Kruskal 은 리스트로 구현
    edges = []
    for _ in range(E):
        n1, n2, weight = map(int, input().split())

        edges.append((weight, n1, n2))
    edges.sort(key=lambda x: x[0])

    print(f"#{test_case} {kruskal_mst(V, edges)}")
