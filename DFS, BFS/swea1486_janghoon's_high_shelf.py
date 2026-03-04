T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())  # N = 점원의 수, B = 선반의 높이
    heights = list(map(int, input().split()))  # 점원들의 키 리스트

    # 점원들의 키를 조합해서 만들 수 있는 탑의 높이 중
    # 선반의 높이보다 높지만 그 중 가장 작은 탑을 찾는다

    best = 10 ** 9


    def dfs(idx, sum_):
        global best

        # 합계가 기준(B)를 넘으면
        if sum_ >= B:
            best = min(best, sum_)
            return

        # 끝까지 다 돌았으면 return
        if idx == N:
            return

        # 함계가 best를 넘어가면 이미 제외해야 하는 경우
        if sum_ >= best:
            return

        # 다음 숫자를 선택한 경우
        dfs(idx + 1, sum_ + heights[idx])

        # 선택하지 않은 경우
        dfs(idx + 1, sum_)


    dfs(0, 0)
    print(f"#{test_case} {best - B}")

    # stack = deque()
    # for i in range(N):
    #     visited = [False] * (N + 1)
    #     visited[i] = True
    #
    #     stack.append(([heights[i]], heights[i + 1:]))
    #
    # while stack:
    #     selected, remain = stack.pop()
    #     # print(selected)
    #     h_sum = sum(selected)
    #
    #     if h_sum < B and remain:
    #         for j in range(len(remain)):
    #             stack.append((selected + [remain[j]], remain[j + 1:]))
    #
    #     elif h_sum >= B:
    #         best = min(best, h_sum)
