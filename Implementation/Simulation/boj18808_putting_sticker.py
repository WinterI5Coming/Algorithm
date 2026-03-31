"""
스티커를 노트북에 붙이려고 한다.
스티커는 상하좌우로 모두 연결되어 있으며, 스티커가 포함되지 않는 불필요한 행이나 열이 존재하지 않는다.
스티커를 붙이는 방법은 다음과 같다.
    1) 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 붙일 수 있는 곳을 찾는다.
        노트북의 위쪽부터 채워나가려고 할 것이므로, 여러 붙일 수 있는 곳이 있다면 그중에서 "가장 위쪽"을 선택한다.
        가장 위쪽에도 해당되는 곳이 여럿있다면, 그중 "가장 왼쪽"을 선택한다.
    2) 만약 붙일 수 있는 위치가 전혀 없다면 시계방향으로 90도 회전한 뒤 위의 과정을 반복한다.
    3) 이 과정을 네 번 반복하여 0, 90, 180, 270도 회전시켰음에도 없다면 해당 스티커를 버린다.


"""

from pprint import pprint

N, M, K = map(int, input().split())  # 노트북 크기 / 스티커 개수
notebook = [[0] * M for _ in range(N)]


# 2차원 배열 자체를 시계방향으로 90도씩 회전시켜서 좌표를 수집한다.
def rotate_matrix(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    rotated = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            rotated[c][row_len - 1 - r] = matrix[r][c]

    return rotated


# 이제 스티커에 대한 정의를 한다.
# 스티커 정보 저장 (회전 4가지 상태)
stickers = []
for _ in range(K):
    rows, cols = map(int, input().split())
    sticker_rotations = []

    sticker_grid = [list(map(int, input().split())) for _ in range(rows)]

    for _ in range(4):
        coords = [
            (r, c)
            for r in range(len(sticker_grid))
            for c in range(len(sticker_grid[0]))
            if sticker_grid[r][c] == 1
        ]
        sticker_rotations.append(coords)
        sticker_grid = rotate_matrix(sticker_grid)
        # pprint(sticker_grid)

    stickers.append(sticker_rotations)

attached_count = 0

for sticker in stickers:

    placed = False

    # 먼저 노트북에 붙일 수 있는 곳이 있는지 확인하는 것이 우선 -> 그런 다음 없다면 회전 시켜서 다시 확인 -> ...
    for rotation in sticker:

        for base_x in range(N):
            for base_y in range(M):

                placement_cells = []

                for dx, dy in rotation:
                    nx = base_x + dx
                    ny = base_y + dy

                    # 범위 벗어나거나 겹치면 실패
                    if not (0 <= nx < N and 0 <= ny < M) or notebook[nx][ny] == 1:
                        placement_cells.clear()
                        break
                    else:
                        placement_cells.append((nx, ny))

                # 붙이기 성공
                if placement_cells:
                    for x, y in placement_cells:
                        notebook[x][y] = 1
                        attached_count += 1

                    placed = True
                    break

            if placed:
                break

            if placed:
                break

        if placed:
            break

pprint(notebook)
print(attached_count)
