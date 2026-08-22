"""
원숭이는 (0, 0)에서 출발해서 (H - 1, W - 1)까지 가려고 한다.
기본적으로는 4방향(상하좌우)로만 이동할 수 있지만,
    K 번까지는 말처럼 이동(8방향)할 수 있다.
이동하는데 몇 번 걸리는가?

상태 확장 BFS 를 적용해서 푼다.
해당 문제에서 상태는 말로 이동한 것으로 볼 수 있다.
같은 위치에 어느 상태가 존재할 수 있는가?
    => 같은 칸이라도 말의 이동 방법을 몇 번 사용해서 왔는지에 따라 달라질 수 있다. = 이걸 상태로 본다.
"""
from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

monkey_dx = (-1, 1, 0, 0)
monkey_dy = (0, 0, -1, 1)
horse_dx = (-1, -2, -2, -1, 1, 2, 2, 1)
horse_dy = (-2, -1, 1, 2, 2, 1, -1, -2)

visited = [[[False, False] for _ in range(W)] for _ in range(H)]
visited[0][0][0] = True

# (x, y, move, horse_used)
q = deque([(0, 0, 0, 0)])
reachable = False
while q:
    x, y, move, horse_used = q.popleft()

    if x == H - 1 and y == W - 1:
        reachable = True
        print(move)
        break

    if horse_used < K:
        # 말 이동 사용
        for d in range(8):
            nx, ny = x + horse_dx[d], y + horse_dy[d]
            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] != 0 and not visited[nx][ny][horse_used + 1]:
                    visited[nx][ny][horse_used + 1] = True
                    q.append((nx, ny, move + 1, horse_used + 1))

    # 기본 이동
    for d in range(4):
        nx, ny = x + monkey_dx[d], y + monkey_dy[d]
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] != 0 and not visited[nx][ny][horse_used]:
                visited[nx][ny][horse_used] = True
                q.append((nx, ny, move + 1, horse_used))

if not reachable:
    print(-1)
