from collections import deque

n = int(input())
status = list(map(int, input().split()))
status.reverse()

# 큐를 이용하여 시도 bfs [(현재 idx, 이동 횟수)]
# 1칸, 3칸의 두 가지 선택지가 존재한다.

visited = [False] * n
q = deque()

q.append((0, 0))
visited[0] = True

ans = -1

while q:
    idx, cnt = q.popleft()

    if idx == n - 1:
        ans = cnt
        break

    for step in (1, 3):
        n_idx = idx + step
        if n_idx < n and status[n_idx] != 0 and not visited[n_idx]:
            visited[n_idx] = True
            q.append((n_idx, cnt + 1))

print(ans)