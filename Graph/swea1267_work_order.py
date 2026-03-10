# from collections import deque
#
# T = 10
#
# for test_case in range(1, T + 1):
#
#     """
#     V개의 정점에 대한 indegree 를 관리한다.
#
#     indegree 가 0인 항목부터 작업을 시작한다.
#     해당 정점이 가리키고 있는 정점의 indegree 를 감소시킨다.
#     """
#     V, E = map(int, input().split())
#     edge = list(map(int, input().split()))
#
#     tree = [[] for _ in range(V+1)]
#     indegree = [0] * (V + 1)
#     for i in range(E):
#         w1, w2 = edge[i * 2], edge[i * 2 + 1]  # w1이 선행 업무, w1 -> w2
#
#         # if w1 not in tree:
#         #     tree[w1] = []
#
#         tree[w1].append(w2)
#         indegree[w2] += 1
#
#     # print(tree)
#     # print(indegree)
#     q = deque()
#     for v in range(1, V + 1):
#         if indegree[v] == 0:
#             q.append(v)
#
#     result = []
#     while q:
#         now = q.popleft()
#         result.append(now)
#
#         for n in tree[now]:
#             indegree[n] -= 1
#             if indegree[n] == 0:
#                 q.append(n)
#
#     print(f"#{test_case}", end=" ")
#     print(*result)

# -----------------------------------------------------------------------------------------
# [DFS]
T = 1

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))


    def dfs(cur_node):

        visited[cur_node] = True

        for next_ in adj_list[cur_node]:
            if not visited[next_]:
                dfs(next_)

        result.insert(0, cur_node)


    adj_list = [[] for _ in range(V + 1)]
    for i in range(E):
        w1, w2 = edge[2 * i], edge[2 * i + 1]
        adj_list[w1].append(w2)

    visited = [False] * (V + 1)
    result = []

    print(adj_list)
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)

    print(f"#{test_case}", end=" ")
    print(*result)
