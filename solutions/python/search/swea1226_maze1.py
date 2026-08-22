from collections import deque

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]  # "1"(벽), "0"(길), "2"(출발점), "3"(도착점)
    visited = [[False for _ in range(16)] for _ in range(16)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque([(i, j) for i in range(16) for j in range(16) if maze[i][j] == "2"])
    can_escape = False
    while q:
        sx, sy = q.popleft()
        visited[sx][sy] = True

        for d in range(4):
            nx, ny = sx + dx[d], sy + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny] == "3":
                    can_escape = True
                    q.clear()
                    break

                if maze[nx][ny] != "1" and not visited[nx][ny]:
                    q.append((nx, ny))

    print(f"#{test_case} {1 if can_escape else 0}")
