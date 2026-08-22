from collections import deque

"""
pypy 로는 통과했지만 python 으로는 방법을 못 찾고 있다...
"""

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N, M, K = map(int, input().split())
grid = [list(input()) for _ in range(N)]
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

visited[0][0][0] = True

# (x, y, move, break_cnt)
q = deque([(0, 0, 1, 0)])
possible = False
while q:
    x, y, move, break_cnt = q.popleft()

    if x == N - 1 and y == M - 1:
        possible = True
        print(move)
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:

            # 벽을 만났을 때
            if grid[nx][ny] == "1" and break_cnt < K and not visited[nx][ny][break_cnt + 1]:
                visited[nx][ny][break_cnt + 1] = True
                q.append((nx, ny, move + 1, break_cnt + 1))

            # 벽이 아닌 경우
            elif grid[nx][ny] == "0" and not visited[nx][ny][break_cnt]:
                visited[nx][ny][break_cnt] = True
                q.append((nx, ny, move + 1, break_cnt))

if not possible:
    print(-1)
