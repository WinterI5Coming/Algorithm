from collections import deque

N, K = map(int, input().split())

MAX = 10 ** 5
dist = [-1] * (MAX + 1)
prev = [-1] * (MAX + 1)
dist[N] = 0

q = deque([N])
find = False
while q:
    cur = q.popleft()

    if cur == K:
        break

    options = (cur - 1, cur + 1, cur * 2)
    for o in options:
        if 0 <= o <= MAX and dist[o] == -1:
            dist[o] = dist[cur] + 1
            prev[o] = cur
            q.append(o)

print(dist[K])

path = [K]
idx = K
for _ in range(dist[K]):
    path.append(prev[idx])
    idx = prev[idx]
path.reverse()
print(*path)
