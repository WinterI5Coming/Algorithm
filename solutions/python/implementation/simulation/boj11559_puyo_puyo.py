from collections import deque


grid = [list(input()) for _ in range(12)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(sx, sy, visited):
    color = grid[sx][sy]
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    group = [(sx, sy)]

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if grid[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    group.append((nx, ny))

    return group


def gravity():
    for j in range(6):
        pieces = []
        for i in range(11, -1, -1):
            if grid[i][j] != ".":
                pieces.append(grid[i][j])

        for i in range(11, -1, -1):
            if pieces:
                grid[i][j] = pieces.pop(0)
            else:
                grid[i][j] = "."


chain_pop = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    del_list = []

    for i in range(12):
        for j in range(6):
            if grid[i][j] == "." or visited[i][j]:
                continue

            group = bfs(i, j, visited)
            if len(group) >= 4:
                del_list.extend(group)

    if not del_list:
        break

    for x, y in del_list:
        grid[x][y] = "."

    gravity()
    chain_pop += 1

print(chain_pop)


# grid = [list(input()) for _ in range(12)]

# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)

# chain_pop = 0

# while True:

#     del_list = []
#     for i in range(12):
#         for j in range(6):
#             if grid[i][j] == ".":
#                 continue

#             color = grid[i][j]
#             q = deque([(i, j)])
#             same_color = [(i, j)]
#             while q:
#                 x, y = q.popleft()

#                 for d in range(4):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if (0 <= nx < 12 and 0 <= ny < 6):
#                         if grid[nx][ny] == color and (nx, ny) not in same_color:
#                             same_color.append((nx, ny))
#                             q.append((nx, ny))

#             if len(same_color) >= 4:
#                 del_list += same_color

#     if not del_list:
#         break
#     else:
#         chain_pop += 1
#         for del_x, del_y in del_list:
#             grid[del_x][del_y] = "."

#         for j in range(6):
#             for i in range(11, -1, -1):
#                 if grid[i][j] == ".":

#                     for k in range(i - 1, -1, -1):
#                         if grid[k][j] != ".":
#                             grid[i][j] = grid[k][j]
#                             grid[k][j] = "."
#                             break

# print(chain_pop)
