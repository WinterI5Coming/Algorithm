"""
수빈이는 현재 점 N, 동생은 점 K에 있다.
수빈이가 선택할 수 있는 행동은 두 가지가 있다.
    => 걷는 것 : 1초후 X-1 또는 X+1로 이동가능
    => 순간이동 : 0초후 2*X로 이동

가장 빠르게 찾을 수 있다면 언제인가
"""

from collections import deque


N, K = map(int, input().split())

MAX = 10**5
dist = [-1] * (MAX + 1)
dist[N] = 0

q = deque([N])
while q:
    cur_pos = q.popleft()

    # 목표 도달 시 바로 종료
    if cur_pos == K:
        print(dist[cur_pos])
        break

    # 순간이동 (가중치 0)
    # 비용이 0이기 대문에 더 빠른 경로이다.
    # => 큐의 앞쪽에 넣어야 다음에 바로 처리된다.
    nxt = cur_pos * 2
    if 0 <= nxt <= MAX and dist[nxt] == -1:
        dist[nxt] = dist[cur_pos]
        q.appendleft(nxt)

    # 왼쪽 이동 + 오른쪽 이동 (가중치 1)
    # 비용이 1이기 때문에 나중에 처리된다.
    nxt = cur_pos - 1
    if 0 <= nxt <= MAX and dist[nxt] == -1:
        dist[nxt] = dist[cur_pos] + 1
        q.append(nxt)

    nxt = cur_pos + 1
    if 0 <= nxt <= MAX and dist[nxt] == -1:
        dist[nxt] = dist[cur_pos] + 1
        q.append(nxt)
