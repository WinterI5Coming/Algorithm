T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 인접 리스트 생성
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())

        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # print(adj_list)

    """
    1 => 1 - 2 - 5
           - 5 - 
    """


    def dfs(person_num):

        visited[person_num] = True

        for p in adj_list[person_num]:
            if not visited[p]:
                dfs(p)


    group_cnt = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            group_cnt += 1
            dfs(i)

    # def bfs(person_num):
    #
    #     visited[person_num] = True # 방문 처리
    #     q = deque([person_num])
    #
    #     while q:
    #         p_num = q.popleft()
    #
    #         for p in adj_list[p_num]:
    #             # 현재 마을과 연결되어 있는 마을들에서 방문하지 않은 곳을 찾아간다
    #             if not visited[p]:
    #                 visited[p] = True
    #                 q.append(p)
    #
    #
    # group_cnt = 0
    # visited = [False] * (N + 1)
    # for i in range(1, N + 1):
    #     # 마을 방문 시작
    #     if not visited[i]:
    #         group_cnt += 1
    #         bfs(i)

    print(f"#{test_case} {group_cnt}")
