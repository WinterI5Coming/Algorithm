from collections import deque

T = int(input())

# 전체 시간복잡도
# 테스트케이스가 T개이고, 각 테스트케이스마다 BFS를 수행한다.
# BFS의 시간복잡도는 O(V + E)인데,
# 이 문제에서는 체스판의 모든 칸이 정점(V)이 된다.
#
# V = I^2  (체스판의 칸 수)
#
# 각 칸에서 최대 8개의 나이트 이동을 확인하므로
# E ≈ 8 * I^2
#
# 따라서 BFS 시간복잡도
# O(V + E) = O(I^2 + 8I^2) = O(I^2)
#
# 전체 시간복잡도
# O(T * I^2)

for test_case in range(1, T + 1):
    I = int(input())
    cur_pos = tuple(map(int, input().split()))
    end_pos = tuple(map(int, input().split()))

    visited = [[False for _ in range(I)] for _ in range(I)]
    visited[cur_pos[0]][cur_pos[1]] = True

    # 나이트의 움직임
    dx = (-1, -2, -2, -1, 1, 2, 2, 1)
    dy = (-2, -1, 1, 2, -2, -1, 1, 2)

    q = deque()
    q.append((cur_pos, 0))
    best = 0
    while q:
        pos, move = q.popleft()

        if pos[0] == end_pos[0] and pos[1] == end_pos[1]:
            best = move
            break

        for d in range(8):
            nx, ny = pos[0] + dx[d], pos[1] + dy[d]
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append(((nx, ny), move + 1))

    print(best)
