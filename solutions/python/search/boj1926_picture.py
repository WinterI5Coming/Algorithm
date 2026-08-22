from collections import deque

n, m = map(int, input().split())  # n = 도화지의 세로 크기, m = 도화지의 가로 크기
picture_grid = [list(map(int, input().split())) for _ in range(n)]

# 1로 연결된 것을 하나의 그림으로 본다. (가로, 세로 까지만)
# 그림의 개수와 가장 넓은 그림의 넓이 모두 출력한다. (단, 그림이 하나도 없다면 가장 넓은 그림의 넓이는 0이다)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# area_list = []  # ❌ (부족/오류) 이제는 cnt/best로 관리하는데 area_list를 더 이상 안 채움
#    => 아래 출력에서 area_list를 쓰면 항상 0, 0이 나오거나(max 에러 방지로 0) 오답이 됨
# ✅ 해결: area_list 자체를 삭제하거나, 정말 쓰려면 area_list.append(bfs(...))로 채워야 함

def bfs(sx, sy):
    q = deque([(sx, sy)])
    picture_grid[sx][sy] = 0  # ✅ 방문처리(중복 방문 방지) - visited 배열 대신 grid를 0으로 바꾸는 방식
    area = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and picture_grid[nx][ny] == 1:
                picture_grid[nx][ny] = 0
                q.append((nx, ny))
                area += 1

    return area


# def search_picture(x, y, que):
#     global area
#
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if (0 <= nx < n and 0 <= ny < m) and picture_grid[nx][ny] == 1:
#             picture_grid[nx][ny] = 0
#             que.append((nx, ny))
#             area += 1
# ❌ (이전 코드에서 부족했던 핵심 포인트)
# 1) global area로 전역 상태를 바꾸는 구조라 위험함 (초기화 위치 실수하면 바로 오답)
# 2) que 인자를 받는데, 내부에서 전역 q를 쓰면(이전 코드) 함수 인터페이스가 깨짐
# ✅ 지금 bfs()처럼 "면적을 리턴"하는 구조가 정석

cnt = 0
best = 0
for i in range(n):
    for j in range(m):
        v = picture_grid[i][j]
        if v == 1:
            cnt += 1
            best = max(best, bfs(i, j))  # ✅ 그림 하나의 넓이를 bfs가 리턴 -> best 갱신

# print(len(area_list))  # ❌ (부족/오류) area_list는 빈 리스트 그대로라 항상 0 출력(오답)
# print(max(area_list) if len(area_list) > 0 else 0)  # ❌ (부족/오류) 여기도 best가 아니라 area_list 기준이라 오답

# ✅ 정답 출력은 아래처럼 해야 함:
print(cnt)
print(best)
