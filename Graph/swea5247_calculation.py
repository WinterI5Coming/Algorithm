from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    INF = float("inf")
    dist = [INF] * (10 ** 6 + 1)
    dist[N] = 0
    q = deque([(N, 0)])
    while q:
        cur_num, move = q.popleft()

        if cur_num == M:
            print(f"#{test_case} {move}")
            break

        option = (cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10)
        for o in option:
            if o >= len(dist) or o < 0:
                continue

            if dist[o] > move + 1:
                dist[o] = move + 1
                q.append((o, move + 1))
