import heapq

T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())

        adj_list[s].append((e, w))

    INF = float("inf")
    dist = [INF] * (N + 1)
    dist[0] = 0
    heap = []
    heapq.heappush(heap, (0, 0))  # (move, cur_node)
    while heap:
        move, cur_node = heapq.heappop(heap)

        if cur_node == N:
            print(f"#{test_case} {move}")
            break

        if move > dist[cur_node]:
            continue

        for nxt_node, weight in adj_list[cur_node]:

            new_move = move + weight
            if dist[nxt_node] > new_move:
                dist[nxt_node] = new_move
                heapq.heappush(heap, (new_move, nxt_node))
