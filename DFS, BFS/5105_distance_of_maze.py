from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    """
    2에서 출발해서 3까지 찾아가야 한다.
    도착이 가능하다면 최소의 칸 수를 출력, 도착할 수 없는 경우에는 0을 출력
    """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sx, sy = None, None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == "2":
                sx, sy = i, j
                break
        else:
            continue
        break

    q = deque()
    q.append((sx, sy, 0))
    maze[sx][sy] = "1"
    best = -1
    while q:
        x, y, move = q.popleft()

        if maze[x][y] == "3":
            best = move
            break

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != "1":
                if maze[nx][ny] == "3":
                    q.append((nx, ny, move))
                    break

                maze[nx][ny] = "1"
                q.append((nx, ny, move + 1))

    print(f"#{test_case} {best if best != -1 else 0}")
