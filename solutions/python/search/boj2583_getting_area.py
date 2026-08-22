"""
M*N 크기의 모눈종이가 존재하고, 이 위에 K개의 직사각형을 그리려고 한다.
K개 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나뉘게 된다.

K개의 직사각형의 좌표가 주어질 때, K개 직사각형 내부를 제외한 나머지가 몇 개의 분리된 영역을 나뉘는가,
그리고 분리된 각 영역의 넓이는 얼마인가를 구한다. (오름차순 출력)

=> M*N 크기의 모눈종이 grid 를 생성한 후, K의 직사각형을 위에 덧칠한다.
    덧칠되지 않은 영역의 수, 넓이를 구한다

"""
from collections import deque

M, N, K = map(int, input().split())
grid = [[0 for _ in range(N)] for _ in range(M)]  # 모눈종이

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())  # y축 [sy, ey), x축 [sx, ex)

    for i in range(sy, ey):
        for j in range(sx, ex):
            if grid[i][j] == 0:
                grid[i][j] = 1

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

cnt = 0
area_list = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:

            cnt += 1  # 영역 수 추가
            area = 1  # 영역 계산
            grid[i][j] = 1  # 방문처리

            q = deque([(i, j)])
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if (0 <= nx < M and 0 <= ny < N) and grid[nx][ny] != 1:
                        area += 1
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            area_list.append(area)

area_list.sort()

print(cnt)
print(*area_list)

"""
[[0, 0, 0, 0, 1, 1, 0],
 [0, 1, 0, 0, 1, 1, 0],
 [1, 1, 1, 1, 0, 0, 0],
 [1, 1, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]]
"""
