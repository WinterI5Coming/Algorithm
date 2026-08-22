import heapq

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    INF = float("inf")
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    heap = []
    heapq.heappush(heap, (0, grid[0][0], 0, 0))  # (cost, cur_height, x, y)
    min_cost = INF
    while heap:
        cost, cur_height, x, y = heapq.heappop(heap)

        # 종료 조건
        if x == N - 1 and y == N - 1:
            min_cost = min(min_cost, cost)
            break

        if cost > dist[x][y]:
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:

                if cur_height < grid[nx][ny]:
                    need = grid[nx][ny] - cur_height
                    new_cost = cost + need + 1

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, grid[nx][ny], nx, ny))

                else:
                    new_cost = cost + 1

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, grid[nx][ny], nx, ny))

    print(f"#{test_case} {min_cost}")
