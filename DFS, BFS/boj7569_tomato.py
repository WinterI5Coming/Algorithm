from collections import deque

"""
가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보가 주어진다.
0 -1 0 0 0

3차원 행렬 어떻게 표현할 것인가
[[
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
],
[
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
]]
grid[z][x][y] => z층에 있는 상자(행렬)의 x, y에 있는 토마토

상하좌우(4방향) 뿐만 아니라 위층 아래층도 확인해야 한다
z - 1, z + 1
"""
M, N, H = map(int, input().split())  # M = 상자의 가로, N = 상자의 세로, H = 쌓아올린 상자 수

grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dz = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dy = (0, 0, 0, 0, -1, 1)

q = deque([(z, x, y) for z in range(H) for x in range(N) for y in range(M) if grid[z][x][y] == 1])
cnt_0 = sum([sum([row.count(0) for row in box]) for box in grid])
days = 0
while q:
    for _ in range(len(q)):  # 하루를 체크해주는 for 문
        sz, sx, sy = q.popleft()

        visited[sz][sx][sy] = True

        for d in range(6):
            nz, nx, ny = sz + dz[d], sx + dx[d], sy + dy[d]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:  # 범위 이내이고
                if not visited[nz][nx][ny] and grid[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = True
                    is_changed = True
                    cnt_0 -= 1

                    q.append((nz, nx, ny))

    if q:
        # q에 원래 들어있는 항목들이 다 빠지고도 여전히 존재한다는 것은
        # => 다음날에 익을 수 있는 토마토들이 여전히 존재한다는 것을 의미한다.
        # => 따라서 다음날로 넘어간다.
        days += 1

print(days if cnt_0 == 0 else -1)
