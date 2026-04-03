"""
R*C인 집이 있고, 각 칸에는 미세먼지의 양을 알 수 있는 수치가 있다.
공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다.

1초 동안 다음의 일이 순서대로 발생한다.
    1) 미세먼지가 확산된다. 확산은 모든 칸에서 동시에 발생한다.
        - 인접 4칸으로 확산된다.
        - 확산되는 양은 = (해당 칸에 존재하는 미세먼지의 양) // 5
        - 해당 칸에 남는 양은 = (해당 칸에 존재했던 미세먼지 - 확산된 양)

    2) 공기청정기가 작동한다.
        - 바람이 나오는데,
            위쪽 공기청정기의 바람은 반시계방향, 아래쪽 공기청정기의 바람은 시게방향으로 순환한다.
            바람이 나오면 바람의 방향대로 이동.

"""

"""
미세먼지 위치에 대한 (i,j) 좌표 수집


1. 1초의 시간이 흐른다.
2. 먼저 모든 미세먼지가 확산된다.
3. 공기청정기가 작동한다.
4. 바람의 경로에 있는 먼지들을 이동시킨다.
"""


def main():
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    # 공기청정기 위치 탐색 (-1로 표시된 행)
    # upper: 위쪽 공기청정기 행 인덱스
    # lower: 아래쪽 공기청정기 행 인덱스
    air = []
    for i in range(R):
        if board[i][0] == -1:
            air.append(i)
    upper = air[0]
    lower = air[-1]

    # 확산 방향: 우, 상, 좌, 하 (행, 열 기준)
    dx = (0, -1, 0, 1)
    dy = (1, 0, -1, 0)

    while T > 0:
        T -= 1

        # ── 1단계: 미세먼지 확산 ──────────────────────────────
        # 확산은 모든 칸에서 동시에 일어나므로
        # 원본 board는 읽기 전용으로 두고, new_board에 결과를 누적
        new_board = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if board[i][j] > 0:  # 먼지가 있는 칸만 처리
                    dust = board[i][j]
                    divided_dust = dust // 5  # 한 방향으로 확산되는 양

                    divided = 0  # 실제로 확산된 총량 누적
                    for d in range(4):
                        n_dust_x, n_dust_y = i + dx[d], j + dy[d]

                        # 범위 체크 + 공기청정기 칸(-1) 제외
                        if 0 <= n_dust_x < R and 0 <= n_dust_y < C:
                            if (
                                board[n_dust_x][n_dust_y] == -1
                            ):  # ← 원본 board 기준으로 체크해야 정확
                                continue
                            new_board[n_dust_x][n_dust_y] += divided_dust
                            divided += divided_dust

                    # 확산하고 남은 먼지를 현재 칸에 기록
                    new_board[i][j] += dust - divided

        # ── 2단계: 공기청정기 작동 ───────────────────────────
        # 바람 방향대로 먼지를 한 칸씩 밀어냄
        # 이동 순서가 중요: 덮어쓰기 전에 먼저 당겨야 함

        # 위쪽 공기청정기: 반시계 방향
        #
        #   [air] → → → →
        #     ↑           ↓
        #     ↑           ↓
        #   [air] ← ← ← ←
        #
        # 왼쪽 열: 위로 당김 (upper-1 → 1)
        for i in range(upper - 1, 0, -1):
            new_board[i][0] = new_board[i - 1][0]
        # 윗 행: 왼쪽으로 당김 (0 → C-2)
        for j in range(C - 1):
            new_board[0][j] = new_board[0][j + 1]
        # 오른쪽 열: 아래로 당김 (0 → upper-1)
        for i in range(upper):
            new_board[i][C - 1] = new_board[i + 1][C - 1]
        # upper 행: 오른쪽으로 당김 (C-1 → 2)
        for j in range(C - 1, 1, -1):
            new_board[upper][j] = new_board[upper][j - 1]
        # 공기청정기 바로 옆 칸은 항상 0 (깨끗한 바람이 나오는 곳)
        new_board[upper][1] = 0

        # 아래쪽 공기청정기: 시계 방향
        #
        #   [air] ← ← ← ←
        #     ↓           ↑
        #     ↓           ↑
        #   [air] → → → →
        #
        # 왼쪽 열: 아래로 당김 (lower+1 → R-2)
        for i in range(lower + 1, R - 1):
            new_board[i][0] = new_board[i + 1][0]
        # 아랫 행: 왼쪽으로 당김 (0 → C-2)
        for j in range(C - 1):
            new_board[R - 1][j] = new_board[R - 1][j + 1]
        # 오른쪽 열: 위로 당김 (R-1 → lower+1)
        for i in range(R - 1, lower, -1):
            new_board[i][C - 1] = new_board[i - 1][C - 1]
        # lower 행: 오른쪽으로 당김 (C-1 → 2)
        for j in range(C - 1, 1, -1):
            new_board[lower][j] = new_board[lower][j - 1]
        # 공기청정기 바로 옆 칸은 항상 0
        new_board[lower][1] = 0

        # 공기청정기 위치는 항상 -1 유지
        new_board[upper][0] = -1
        new_board[lower][0] = -1

        board = new_board

    # -1인 공기청정기 칸 제외하고 먼지 총합 출력
    print(sum(v for row in board for v in row if v > 0))


main()
