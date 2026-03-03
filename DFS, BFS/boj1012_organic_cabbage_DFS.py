from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    """
    해당 버전은 DFS로 해결하는 것이다.
    """

    M, N, K = map(int, input().split())  # M = 밭 가로 길이, N = 밭 세로 길이, K = 배추 심어져 있는 위치 개수

    cabbages = set()
    for _ in range(K):
        y, x = map(int, input().split())
        cabbages.add((x, y))

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    cnt = 0
    while cabbages:
        sx, sy = cabbages.pop()

        stack = deque([(sx, sy)])
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (nx, ny) in cabbages:
                    cabbages.remove((nx, ny))
                    stack.append((nx, ny))
        cnt += 1

    print(cnt)