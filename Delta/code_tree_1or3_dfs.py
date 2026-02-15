n = int(input())
status = list(map(int, input().split()))
status.reverse()

# print(status)

# 첫번째 칸 부터 진행한다
# 모든 경우의 수를 stack으로 관리
# [(현재 위치, 이동 횟수, 성공 여부)]
stack = [(0, 0)]
INF = 10**18
dist = [INF] * n
min_cnt = n + 1

while stack:
    idx, m_cnt = stack.pop()

    if m_cnt > min_cnt:
        continue

    if idx == n - 1:
        continue

    if idx != n - 1:
        # 현재 idx 에서 이동 경우의 수 판단
        # (idx + 1) idx로 이동
        # (idx + 3) idx로 이동
        if idx + 1 < n and status[idx + 1] != 0:
            new_m_cnt = m_cnt + 1
            dist[idx + 1] = new_m_cnt
            stack.append((idx + 1, new_m_cnt))

        if idx + 3 < n and status[idx + 3] != 0:
            new_m_cnt = m_cnt + 1
            dist[idx + 3] = new_m_cnt
            stack.append((idx + 3, new_m_cnt))

print(dist[-1] if dist[-1] != INF else -1)
