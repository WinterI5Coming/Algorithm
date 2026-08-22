from collections import deque

T = int(input())

pipe = {
    0: [0, 1, 2, 3],
    1: [0, -1, 2, -1],
    2: [-1, 1, -1, 3],
    3: [0, 1, -1, -1],
    4: [-1, 1, 2, -1],
    5: [-1, -1, 2, 3],
    6: [0, -1, -1, 3]
}
# 상(0)우(1)하(2)좌(3)
# pipe_type[type - 1][진입구역] = 탈출구역
pipe_type = {
    0: [2, 3, 0, 1],
    1: [2, -1, 0, -1],
    2: [-1, 3, -1, 1],
    3: [1, 0, -1, -1],
    4: [-1, 2, 1, -1],
    5: [-1, -1, 3, 2],
    6: [3, -1, -1, 0]
}


def move(x, y, to_dir, from_dir):
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    nx, ny = x + dx[to_dir], y + dy[to_dir]
    if (0 <= nx < N and 0 <= ny < M) and not visited[nx][ny] and grid[nx][ny] != 0:
        if pipe_type[grid[nx][ny] - 1][from_dir] != -1:
            return nx, ny, from_dir
    return -1, -1, -1


def rev(dir_):
    return (dir_ + 2) % 4


for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True

    # 이동하기 전 조건
    # 1) 현재 위치하고 있는 파이프는 어디로 뚫려 있는가
    # 2) 내가 뚫려있는 방향으로 이동했을 때 이동한 곳의 파이프도 뚤려 있던가
    #        + 방문했던 곳은 아닌가

    possible_spot = 1
    q = deque()
    for to_dir in pipe[grid[R][C] - 1]:
        if to_dir != -1:
            q.append((R, C, to_dir))
            # nx, ny, from_dir = move(R, C, to_dir, rev(to_dir))
            # if (nx, ny, from_dir) != (-1, -1, -1):
            #     possible_spot += 1
            #     visited[nx][ny] = True
            #     q.append((nx, ny, from_dir))

    for _ in range(L + 1):
        x, y, to_dir = q.popleft()

        pipe_num = grid[x][y]
        for to_dir in pipe[pipe_num - 1]:
            nx, ny, from_dir = move(x, y, to_dir, rev(to_dir))
            if (nx, ny, from_dir) != (-1, -1, -1):
                possible_spot += 1
                visited[nx][ny] = True
                q.append((nx, ny, from_dir))

    print(f"#{test_case} {possible_spot}")