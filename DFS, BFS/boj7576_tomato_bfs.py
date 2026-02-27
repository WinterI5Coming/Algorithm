from collections import deque

M, N = map(int, input().split())
box_grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt_0 = sum([1 for i in range(N) for j in range(M) if box_grid[i][j] == 0])

q = deque((i, j) for i in range(N) for j in range(M) if box_grid[i][j] == 1)

days = 0
while q:
    size = len(q)

    is_changed = False
    for _ in range(size):
        sx, sy = q.popleft()

        for d in range(4):
            nx, ny = sx + dx[d], sy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and box_grid[nx][ny] == 0:
                cnt_0 -= 1
                box_grid[nx][ny] = 1
                q.append((nx, ny))
                is_changed = True

    if is_changed:
        days += 1

    if cnt_0 == 0:
        print(days)
        break
else:
    print(-1)
