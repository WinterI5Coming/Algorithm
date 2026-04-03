# [개선버전]
"""
아래의 시간초과의 원인에는 몇 가지 요인이 존재했다.
1) 한 번의 순회가 끝나고 새 빙산 좌표를 구하는 과정에서 다음의 방법을 사용했었다.
    => icebergs = [(i, j) for i in range(N) for j in range(M) if grid[i][j] != 0]
    => 이렇게 되면 전체 배열을 매번 또 순회하는 것이기 때문에 손실이 크다. 우리는 전체 배열을 순회하지 않도록 하는게 목적!

2) 방향(델타) 탐색 for문을 풀어서 썼다.
    => 반복문의 오버헤드가 발생한다.
    => range(4)의 반복 + 매 반복 마다 dx[d], dy[d] 인덱싱 + 덧셈 2번 + 튜플/값 할당
    => 위의 비용들을 반복문 없이 쓰게 되면, 반복문 자체가 없기도 하고, 리스트/튜플 인덱싱 없고, 산술연산만이 있다.

3) visited를 set으로 관리한 것
    => 기존에 set을 쓰던 방식은 (nx, ny) 튜플 생성과 해시 비용(set, in)이 발생한다.
    => 이걸 그냥 visited 배열을 만들어 놓고 새로운 값을 덮어씌우는 방식으로 변환
"""
from collections import deque


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

icebergs = [(i, j) for i in range(N) for j in range(M) if grid[i][j] != 0]

visited = [[0] * M for _ in range(N)]
mark = 0

years = 0
divided = False
while not divided:
    if not icebergs:
        years = 0
        break

    start_point = icebergs[0]
    mark += 1
    visited[start_point[0]][start_point[1]] = mark
    q = deque([start_point])

    connected_cnt = 1
    while q:
        x, y = q.popleft()

        nx = x - 1
        if 0 <= nx < N and grid[nx][y] != 0 and visited[nx][y] != mark:
            visited[nx][y] = mark
            connected_cnt += 1
            q.append((nx, y))

        nx = x + 1
        if 0 <= nx < N and grid[nx][y] != 0 and visited[nx][y] != mark:
            visited[nx][y] = mark
            connected_cnt += 1
            q.append((nx, y))

        ny = y - 1
        if 0 <= ny < M and grid[x][ny] != 0 and visited[x][ny] != mark:
            visited[x][ny] = mark
            connected_cnt += 1
            q.append((x, ny))

        ny = y + 1
        if 0 <= ny < M and grid[x][ny] != 0 and visited[x][ny] != mark:
            visited[x][ny] = mark
            connected_cnt += 1
            q.append((x, ny))

    if connected_cnt != len(icebergs):
        divided = True
        break

    adj_sea = []
    for ice_x, ice_y in icebergs:
        sea = 0

        ice_nx = ice_x - 1
        if 0 <= ice_nx < N and grid[ice_nx][ice_y] == 0:
            sea += 1

        ice_nx = ice_x + 1
        if 0 <= ice_nx < N and grid[ice_nx][ice_y] == 0:
            sea += 1

        ice_ny = ice_y - 1
        if 0 <= ice_ny < M and grid[ice_x][ice_ny] == 0:
            sea += 1

        ice_ny = ice_y + 1
        if 0 <= ice_ny < M and grid[ice_x][ice_ny] == 0:
            sea += 1

        adj_sea.append(sea)

    new_icebergs = []
    for i in range(len(icebergs)):
        ice_point, melt = icebergs[i], adj_sea[i]
        cur_height = grid[ice_point[0]][ice_point[1]]

        if cur_height - melt <= 0:
            grid[ice_point[0]][ice_point[1]] = 0

        else:
            grid[ice_point[0]][ice_point[1]] = cur_height - melt
            new_icebergs.append((ice_point[0], ice_point[1]))

    icebergs = new_icebergs
    years += 1

print(years)


# ------------------------------------------------------------------------------
# [시간초과]
# from collections import deque


# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]

# """
# 1) 초기 상태
# - 배열을 입력받고, 빙산이 존재하는 좌표들을 icebergs 리스트에 저장한다.
# - 이후 모든 연산은 icebergs를 기준으로 진행한다.

# 2) 영역 수 계산 (분리 여부 확인)
# - icebergs 중 하나의 좌표를 시작점으로 BFS 수행
# - BFS를 통해 연결된 빙산의 개수 connected_cnt를 센다.
# - 만약 connected_cnt != len(icebergs) 이면
#   → 빙산이 2덩어리 이상으로 분리된 상태
#   → 현재 years 출력 후 종료

# 3) 종료 조건 확인
# - 만약 icebergs가 비어있다면
#   → 빙산이 전부 녹은 것
#   → 0 출력 후 종료

# 4) 각 빙산 칸의 녹는 양 계산
# - icebergs 리스트를 순회하면서
#   각 좌표에 대해 상하좌우를 확인
# - 인접한 바다(0)의 개수를 세어 adj_sea 리스트에 저장

# 5) 빙산 녹이기 (동시 갱신)
# - icebergs를 다시 순회하면서
#   height - adj_sea 만큼 감소
# - 이때 반드시 “한꺼번에” 반영해야 함
# - 녹은 결과가 0 이하이면 0으로 처리

# 6) 다음 해 빙산 좌표 갱신
# - 녹인 결과가 0보다 큰 칸만 new_icebergs에 추가
# - icebergs = new_icebergs 로 갱신

# 7) 시간 증가
# - years += 1

# 8) 반복
# - 위 과정을 빙산이 분리되거나 전부 녹을 때까지 반복
# """
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)

# icebergs = [(i, j) for i in range(N) for j in range(M) if grid[i][j] != 0]

# years = 0
# divided = False
# while not divided:
#     # 만약 icebergs가 비어있는 경우 => 모든 빙산이 녹아버린 것
#     if not icebergs:
#         years = 0
#         break

#     start_point = icebergs[0]
#     q = deque([start_point])

#     visited = set()
#     visited.add(start_point)

#     connected_cnt = 1
#     while q:
#         sx, sy = q.popleft()

#         for d in range(4):
#             nx, ny = sx + dx[d], sy + dy[d]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if (nx, ny) not in visited and grid[nx][ny] != 0:

#                     connected_cnt += 1
#                     visited.add((nx, ny))
#                     q.append((nx, ny))

#     if len(icebergs) != connected_cnt:
#         # 실제 존재하는 빙산 좌표의 개수와 특정 점에서 시작해서 빙산을 탐색할 때의 수가 같지 않으면
#         # => 빙산이 2부분 이상으로 갈라졌다는 것을 의미한다.
#         divided = True
#         break

#     # 각 빙산 좌표에 인접한 바다의 수 세기
#     adj_sea = []
#     for ice_x, ice_y in icebergs:

#         sea = 0
#         for d in range(4):
#             ice_nx, ice_ny = ice_x + dx[d], ice_y + dy[d]
#             if (0 <= ice_nx < N and 0 <= ice_ny < M) and grid[ice_nx][ice_ny] == 0:
#                sea += 1

#         adj_sea.append(sea)

#     # 녹이기
#     new_icebergs = []
#     for i in range(len(icebergs)):
#         ice_point, melt = icebergs[i], adj_sea[i]
#         cur_height = grid[ice_point[0]][ice_point[1]]

#         if cur_height - melt <= 0:
#             grid[ice_point[0]][ice_point[1]] = 0
#         else:
#             grid[ice_point[0]][ice_point[1]] = cur_height - melt
#             new_icebergs.append((ice_point[0], ice_point[1]))

#     # 해 지난다
#     icebergs = new_icebergs
#     years += 1

# print(years)
