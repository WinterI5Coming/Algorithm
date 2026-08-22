from collections import deque
from pprint import pprint
from typing import Deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    # pprint(maze)

    """
    출발지에서 시작해서 목적지에 도작하는 경로가 존재하는지 확인한다.
    도착할 수 있다면 1, 아니면 0을 출력
    
    2에서 출발해서 0인 통로를 따라서 3으로 도착할 수 있어야 한다. (1은 벽)
    """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque((i, j) for i in range(N) for j in range(N) if maze[i][j] == "2")
    # print(q)

    is_possible = False
    while q:
        x, y = q.popleft()

        if is_possible:
            break

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != "1":
                if maze[nx][ny] == "3":
                    is_possible = True
                maze[nx][ny] = "1"
                q.append((nx, ny))

    print(f"#{test_case} {1 if is_possible else 0}")