from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

# (0, 0) 에서 (N-1, M-1)로 이동해야 한다

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 함수 인자로 que를 전달받고 있는데, BFS는 사실상 함수가 큐를 내부에서 만들어도 된다.
# => 밖에서 만들어서 넘기면,
#           1) 상태가 분산되고,
#           2) 재사용성 떨어지고,
#           3) 실수 가능성만 늘어나게 된다
def find_way(x, y, que):
    # global best

    # (0, 0)을 출발하면서 0으로 만들고 출발한다
    maze[x][y] = "0"
    # 현재 위치, 이동한 거리

    que.append((x, y, 1))
    # que.append(([x, y], 1))
    # => 좌표를 리스트로 넣는것 보다 불변/가벼운 튜플이 정석적이고 더 안전하다
    # => 1(move)를 큐에 같이 넣는 방식도 가능하지만,
    #       보통은 dist 배열을 두거나, maze를 숫자로 바꿔서 거리를 직접 기록하는게 더 깔끔하다

    while que:
        cur_x, cur_y, move = que.popleft()

        # if move > best:
        #     continue
        # => BFS는 목표에 처음 도착한 순간이 최단거리로 볼 수 있기 때문에 가지치기 불필요하다

        if cur_x == N - 1 and cur_y == M - 1:
            # best = min(best, move)
            return move

        for d in range(4):
            nx, ny = cur_x + dx[d], cur_y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == "1":
                maze[nx][ny] = "0"
                que.append((nx, ny, move + 1))


q = deque()
print(find_way(0, 0, q))
