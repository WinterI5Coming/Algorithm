"""
고층 건물은 F 층으로 이루어져 있고, 스타트링크는 G 층, 강호가 있는 곳은 S 층이다.
엘리베이터를 타고 이동할 수 있지만 버튼은 2개밖에 없다.
    U 버튼은 위로 U층 만큼 가는 버튼, D 버튼은 아래로 D층 만큼 가는 버튼

적어도 몇 번을 눌러야 갈 수 있는지 구한다. 엘리베이터를 이용해서 갈 수 없다면, "use the stairs" 출력

도착할 수 없다는 걸 어떻게 판단할 것인가?
=> 방문처리를 하는 것이 중점 포인트!!!
=> 방문처리를 하지 않으면 올라가고, 내려가는 선택을 반복해서 진행하면서 중복된 층에 계속 도착할 수 있다.
=> 방문처리를 BFS의 본질이라는 것을 잊지 말자
=> 따라서 방문처리를 통해 경우의 수를 줄여야 한다.

- 숨바꼭질과 동일한 문제
"""
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)
visited[S] = True

result = -1
q = deque([(S, 0)])
while q:
    cur_floor, move = q.popleft()

    if cur_floor == G:
        result = move
        break

    for d in (0, 1):
        if d == 0:
            # 위로 간다
            if cur_floor + U <= F and not visited[cur_floor + U]:
                visited[cur_floor + U] = True
                q.append((cur_floor + U, move + 1))

        else:
            # 아래로 간다
            if cur_floor - D >= 1 and not visited[cur_floor - D]:
                visited[cur_floor - D] = True
                q.append((cur_floor - D, move + 1))

print(result if result != -1 else "use the stairs")
