from collections import deque

T = 1

for test_case in range(1, T + 1):
    """
    V개의 정점에 대한 indegree 를 관리한다.

    indegree 가 0인 항목부터 작업을 시작한다.
    해당 정점이 가리키고 있는 정점의 indegree 를 감소시킨다.
    """

    V, E = map(int, input().split())
    edge = list(map(int, input().split()))

    tree = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)
    for i in range(E):
        w1, w2 = edge[2 * i], edge[2 * i + 1]

        tree[w1].append(w2)
        indegree[w2] += 1

    # indegree가 0인것 부터 시작해야 한다.
    q = deque()
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        now = q.popleft()
        result.append(now)

        # now의 후행작업의 indegree 감소
        for n_work in tree[now]:
            indegree[n_work] -= 1
            if indegree[n_work] == 0:
                q.append(n_work)

    print(f"#{test_case}", end=" ")
    print(*result)

# -----------------------------------------------------------------------------------------
# [DFS]
# T = 1
#
# for test_case in range(1, T + 1):
#     V, E = map(int, input().split())
#     edge = list(map(int, input().split()))
#
#
#     def dfs(cur_node):
#
#         visited[cur_node] = True
#
#         for next_ in adj_list[cur_node]:
#             if not visited[next_]:
#                 dfs(next_)
#
#         result.insert(0, cur_node)
#
#
#     adj_list = [[] for _ in range(V + 1)]
#     for i in range(E):
#         w1, w2 = edge[2 * i], edge[2 * i + 1]
#         adj_list[w1].append(w2)
#
#     visited = [False] * (V + 1)
#     result = []
#
#     print(adj_list)
#     for i in range(1, V + 1):
#         if not visited[i]:
#             dfs(i)
#
#     print(f"#{test_case}", end=" ")
#     print(*result)
