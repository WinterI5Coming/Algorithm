from collections import deque

T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split()) # M = 밭 가로 길이, N = 밭 세로 길이, K = 배추 심어져 있는 위치 개수

    """
    지렁이는 배추 근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
    배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한(4방향) 다른 배추로 이동할 수 있어, 다른 배추들도 같이 보호받는다.
    
    즉, 배추가 모여 있는 곳에는 한 마리의 지렁이만 있으면 되기 때문에 몇 군데에 퍼져있는지를 알 수 있으면 된다.
    필요한 최소의 지렁이 수를 구한다.
    """

    grid = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:

                grid[i][j] = 0
                q.append((i, j))

                while q:
                    s_x, s_y = q.popleft()

                    for d in range(4):
                        nx, ny = s_x + dx[d], s_y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            q.append((nx, ny))

                cnt += 1

    print(cnt)