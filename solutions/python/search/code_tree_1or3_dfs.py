n = int(input())
status = list(map(int, input().split()))
status.reverse()

# print(status)

# 첫번째 칸 부터 진행한다
# 모든 경우의 수를 stack으로 관리
# [(현재 위치, 이동 횟수)]
stack = [(0, 0)]
INF = 10 ** 19
dist = [INF] * n
min_cnt = INF

while stack:
    idx, cnt = stack.pop()

    # 가지치기
    # dist에 등록된 같은 idx에 왔는데 더 많은 횟수로 온 경우
    # 예를 들어, 3번째 칸을 한 번에 갈 수 있는 반면, 1칸씩 세번으로 갈 수도 있다
    # 이런 비효율적인 경우는 제외해줘야 한다
    # 1칸을 먼저 하고 3칸을 나중에 하기 때문에
    if cnt > dist[idx]:
        continue

    # idx가 끝이면 이동 완료
    # => min_cnt 갱신
    if idx == n - 1:
        min_cnt = min(min_cnt, cnt)
        continue

    # 현재 idx 에서 이동 경우의 수 판단
    # (idx + 1) idx로 이동
    # (idx + 3) idx로 이동
    for step in (1, 3):
        n_idx = idx + step
        if n_idx < n and status[n_idx] != 0:
            new_cnt = cnt + 1
            if new_cnt < dist[n_idx]:
                dist[n_idx] = new_cnt
                stack.append((n_idx, new_cnt))

print(min_cnt if min_cnt != INF else -1)
