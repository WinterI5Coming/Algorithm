"""
세로 N, 가로 M 길이의 격자 상자에 토마토를 보관한다.
보관 후 하루가 지났을 때, 익은 토마토(1)들의 인접한 곳(4방향)에 있는 익지 않은 토마토(0)들은 영향을 받아서 익게된다.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다(-1).
토마토들이 며칠이 지나면 다 익을 수 있는지 최소 일수를 구해야 한다.

모든 토마토가 이미 익어 있다면 0, 아니라면 최소날짜, 만약 토마토가 모두 익을 수 없다면 -1 출력
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
box_grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt_0 = sum([1 for i in range(N) for j in range(M) if box_grid[i][j] == 0])
start_point = [(i, j) for i in range(N) for j in range(M) if box_grid[i][j] == 1]
q = deque()


def dfs(cnt, target, days):
    for t in target:
        q.append(t)
    next_ = []

    while q:
        sx, sy = q.popleft()

        for d in range(4):
            nx, ny = sx + dx[d], sy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and box_grid[nx][ny] == 0:
                cnt -= 1
                box_grid[nx][ny] = 1
                next_.append((nx, ny))

    if next_:
        dfs(cnt, next_, days + 1)

    else:
        # print(f"cnt: {cnt}, days: {days}")
        print(days if cnt == 0 else -1)


dfs(cnt_0, start_point, 0)
# print(result)
# print(result[1] if result[0] == 0 else -1)
