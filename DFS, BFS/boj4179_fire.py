from collections import deque

# R: 행, C: 열
R, C = map(int, input().split())

# 미로 입력 (각 칸은 '#', '.', 'J', 'F')
maze = [list(input().strip()) for _ in range(R)]

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지훈이 시작 위치
sx, sy = None, None

# ==============================
# 불이 각 칸에 "언제" 도착하는지 계산
# ==============================

INF = 10 ** 9  # 불이 도착하지 않는 칸 표시용

# fire[r][c] = 해당 칸에 불이 도착하는 최소 시간
fire = [[INF for _ in range(C)] for _ in range(R)]

fire_q = deque()

# 초기 상태 설정
# - 불 시작점은 시간 0
# - 지훈이 시작점 위치 저장
for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            sx, sy = i, j
        elif maze[i][j] == "F":
            fire[i][j] = 0
            fire_q.append((i, j))

# 불 BFS (멀티 소스 BFS)
# 여러 불 시작점에서 동시에 퍼진다고 생각하면 됨
while fire_q:
    fx, fy = fire_q.popleft()

    for d in range(4):
        n_fx, n_fy = fx + dx[d], fy + dy[d]

        # 범위 안이고
        if 0 <= n_fx < R and 0 <= n_fy < C:
            # 벽이 아니고 아직 방문 안 한 칸이면
            if maze[n_fx][n_fy] != "#" and fire[n_fx][n_fy] == INF:
                # 현재 시간 + 1
                fire[n_fx][n_fy] = fire[fx][fy] + 1
                fire_q.append((n_fx, n_fy))

# ==============================
# 사람 BFS (탈출 최단 시간)
# ==============================

# 사람 방문 여부
visited = [[False for _ in range(C)] for _ in range(R)]

person_q = deque()
person_q.append((sx, sy, 0))  # (현재 위치, 시간)
visited[sx][sy] = True

while person_q:
    px, py, move = person_q.popleft()

    # 현재 위치에 불이 이미 도착했다면 사망
    # move 시점에 불이 오거나 먼저 왔다면 이동 불가
    if move >= fire[px][py]:
        continue

    for d in range(4):
        n_px, n_py = px + dx[d], py + dy[d]

        # 격자 밖으로 나가면 탈출 성공
        # BFS이므로 가장 먼저 나간 시간이 최단 시간
        if not (0 <= n_px < R and 0 <= n_py < C):
            print(move + 1)
            exit()

        # 벽이거나 이미 방문한 칸이면 스킵
        if maze[n_px][n_py] == "#" or visited[n_px][n_py]:
            continue

        # 다음 칸이 안전한지 확인
        # 1) 불이 영원히 안 오는 칸이거나
        # 2) 내가 도착하는 시간(move+1)이 불 도착 시간보다 빠른 경우
        if fire[n_px][n_py] == INF or move + 1 < fire[n_px][n_py]:
            visited[n_px][n_py] = True
            person_q.append((n_px, n_py, move + 1))

# 큐가 다 비었는데 탈출 못했으면 불가능
print("IMPOSSIBLE")