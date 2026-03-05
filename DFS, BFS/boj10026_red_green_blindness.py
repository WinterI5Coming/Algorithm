"""
적록색약은 빨간색과 초록색의 차이를 느끼지 못한다.
N*N 그리드에 R, G, B 세 가지의 색이 존재한다.
같은 색상이 상하좌우로 인접해 있는 경우 하나의 구역으로 본다.
적록색약이 아닌 사람과 적록색약이 있는 사람이 봤을 때의 구역 수를 구한다.
"""
from collections import deque

# ----------------------------------------------------------------
# 방법1.
"""
적록색약이 있는 사람의 경우에는 빨간색과 초록색이 동일한 색으로 간주해도 좋다.
따라서 적록색약이 있는 사람을 위한 grid를 따로 만든다.
"""

# N = int(input())
# grid = [list(input()) for _ in range(N)]
# grid_abnormal = [["R" if c == "G" else c for c in row] for row in grid]
# # print(grid)
# # print(grid_abnormal)
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# def bfs(g):
#
#     visited = [[False for _ in range(N)] for _ in range(N)]
#
#     area = 0
#     for i in range(N):
#         for j in range(N):
#
#             if not visited[i][j]:
#
#                 color = g[i][j]
#
#                 visited[i][j] = True
#                 q = deque([(i,j)])
#                 while q:
#                     x, y = q.popleft()
#
#                     for d in range(4):
#                         nx, ny = x + dx[d], y + dy[d]
#                         if 0 <= nx < N and 0 <= ny < N:
#                             if not visited[nx][ny] and g[nx][ny] == color:
#                                 visited[nx][ny] = True
#                                 q.append((nx, ny))
#
#                 area += 1
#
#     return area
#
# print(bfs(grid), bfs(grid_abnormal))

# ----------------------------------------------------------------
# 방법2.
"""
이번 방법에서는 grid를 따로 생성하지 않고 함수에서 인자로 구분한다.

(현재 검사하고 있는 색, 인접한 칸의 색, 색약의 여부)
색약이 없는 경우에는 현재 검사하고 있는 색과 인접한 칸의 색이 같은 경우에만 True를 준다.
색약이 있는 경우
    => 현재 검사하고 있는 색이 "R", "G"인 경우, 들어오는 색이 "R","G" 두 가지 모두 True 준다.
    => "B" 검사하고 있다면 같은 색의 경우에만 True
"""

# N = int(input())
# grid = [list(input()) for _ in range(N)]
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
#
# def is_same_color(c, adj_c, is_abnormal):
#     if not is_abnormal:
#         return c == adj_c
#
#     if c == "B" or adj_c == "B":
#         return c == adj_c
#     return True
#
#     if c == "B":
#         return True if adj_c == "B" else False
#
#     if not is_abnormal:
#         # 색약 없는 경우
#         if c == adj_c:
#             return True
#         else:
#             return False
#
#     elif is_abnormal:
#         # 색약 있는 경우
#         if c == "R" or c == "G":
#             if adj_c == "R" or adj_c == "G":
#                 return True
#             else:
#                 return False
#
#     return True
#
#
# def bfs(abnormal):
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     area = 0
#
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#
#                 color = grid[i][j]
#
#                 visited[i][j] = True
#                 q = deque([(i, j)])
#                 while q:
#                     x, y = q.popleft()
#
#                     for d in range(4):
#                         nx, ny = x + dx[d], y + dy[d]
#                         if 0 <= nx < N and 0 <= ny < N:
#                             if not visited[nx][ny] and is_same_color(color, grid[nx][ny], abnormal):
#                                 visited[nx][ny] = True
#                                 q.append((nx, ny))
#
#                 area += 1
#     return area
#
#
# print(bfs(False), bfs(True))

# ----------------------------------------------------------------
# 방법3.

"""
서로소(DSU) 방법
"""
def same(a, b, abnormal):
    if not abnormal:
        return a == b
    if a == 'B' or b == 'B':
        return a == b
    return True  # R/G는 같은 색으로 취급

def count_regions_dsu(grid, abnormal):
    n = len(grid)
    parent = list(range(n * n))
    size = [1] * (n * n)

    def idx(i, j):
        return i * n + j

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # 오른쪽/아래만 확인해서 같은 구역이면 union
    for i in range(n):
        for j in range(n):
            if j + 1 < n and same(grid[i][j], grid[i][j + 1], abnormal):
                union(idx(i, j), idx(i, j + 1))
            if i + 1 < n and same(grid[i][j], grid[i + 1][j], abnormal):
                union(idx(i, j), idx(i + 1, j))

    # 서로 다른 대표(root) 개수 = 구역 개수
    roots = set()
    for v in range(n * n):
        roots.add(find(v))
    return len(roots)

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

print(count_regions_dsu(grid, False), count_regions_dsu(grid, True))
