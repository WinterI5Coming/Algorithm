import heapq

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    heap = []
    heapq.heappush(heap, (0, 0, 0))

    INF = float("inf")
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    min_time = 0
    while heap:
        time, x, y = heapq.heappop(heap)

        if x == N - 1 and y == N - 1:
            min_time = time
            break

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                new_time = time + int(grid[nx][ny])

                if new_time < dist[nx][ny]:
                    dist[nx][ny] = new_time
                    heapq.heappush(heap, (new_time, nx, ny))

    print(f"#{test_case} {min_time}")
