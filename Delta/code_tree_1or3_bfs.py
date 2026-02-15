from collections import deque

n = int(input())
status = list(map(int, input().split()))
status.reverse()

visited = [False] * n
q = deque()

# 첫번째 칸 부터 진행한다
# 모든 경우의 수를 stack으로 관리
# [(현재 위치, 이동 횟수)]
q.append((0, 0))
visited[0] = True

answer = -1

while q:
    idx, cnt = q.popleft()

    if idx == n - 1:
        answer = cnt
        break

    for step in (1, 3):
        ni = idx + step

        if 0 <= ni < n and status[ni] != 0 and not visited[ni]:
            visited[ni] = True
            q.append((ni, cnt + 1))

print(answer)