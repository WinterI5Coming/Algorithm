def dfs(start):
    visited = [False] * (V + 1)
    stack = [start] # 시작하는 노드를 스택에 넣고 시작한다
    path = []

    while stack:
        cur_node = stack.pop()

        # 현재 노드가 방문하지 않은 노드라면 경로에 추가한다
        if not visited[cur_node]:
            visited[cur_node] = True
            path.append(cur_node)

            # 현재 노드에서 연결된 다른 노드들 중에서 방문하지 않은 노드를 다음 경로로 정한다
            for next_node in adj_list[cur_node]:
                if not visited[next_node]:
                    stack.append(next_node)

    return path


V, E = map(int, input().split())  # V = 정점의 수, E = 간선의 수
edge = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]

# 양방향 그래프 만들기
for i in range(E):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 작은 번호부터 방문해야 한다는 조건을 만족시키기 위해 내림차순으로 정렬을 한다.
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)
print(adj_list)

print(*dfs(1))
