from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    """    
    해당 버전은 격자를 만들지 않고 해결하는 것이다.
    문제에서는 배추의 위치에 대해 전체 밭에 대한 정보를 격자로 제공해 주는 것이 아니라,
    각 배추에 대한 위치 좌표로 알려준다는 점이 존재한다.
    
    이를 위해 우리는 배추의 위치에 대한 좌표를 모두 set을 사용해서 저장한다.
    우리가 필요한건 다음과 같다.
        => 특정 좌표에 배추가 존재하는가? + 이 좌표를 방문했는가?
        => set은 이 조건에 적합하다고 볼 수 있다. 
    """
    M, N, K = map(int, input().split())  # M = 밭 가로 길이, N = 밭 세로 길이, K = 배추 심어져 있는 위치 개수

    cabbages = set()
    for _ in range(K):
        y, x = map(int, input().split())
        cabbages.add((x, y))

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    cnt = 0
    while cabbages:
        sx, sy = cabbages.pop()
        q = deque([(sx, sy)])

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (nx, ny) in cabbages:
                    cabbages.remove((nx, ny))
                    q.append((nx, ny))

        cnt += 1

    print(cnt)
