"""
정사각형 모양의 지도가 존재할 때, => 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
이를 통해 연결된(4방향) 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려고 한다.

총 단지 수를 출력하고, 각 단지내 집 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력한다.
"""
from collections import deque

N = int(input())
grid = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(sx, sy):

    cnt = 1
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    return cnt


house = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == "1" and not visited[i][j]:
            house.append(bfs(i, j))

print(len(house))
for h in range(len(house)):
    print(house[h])
