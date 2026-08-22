from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    """
    N*N 배열에서 한 줄에서 하나씩 N개의 숫자를 고른 합이 최소가 되어야 한다.
    단, 세로로 같은 줄에서 두 개 이상 고를 수 없다.
    
    [] * N 배열로 세로 어떤 열에 방문했는지 관리한다.
    """
    stack = deque()
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        stack.append((visited, 1, matrix[0][i]))

    best = 10**9
    while stack:
        visit, cnt, sum_ = stack.pop()

        if sum_ > best:
            continue

        if cnt == N:
            # 다 고른상황
            best = min(best, sum_)

        else:
            for j in range(N):
                if visit[j]:
                    continue

                n_visit = visit[:]
                n_visit[j] = True
                stack.append((n_visit, cnt + 1, sum_ + matrix[cnt][j]))

    print(f"#{test_case} {best}")
