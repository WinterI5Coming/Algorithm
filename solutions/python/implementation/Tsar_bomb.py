T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    bomb_area = [list(map(int, input().split())) for _ in range(n)]

    # 모든 점을 순회하면서 합을 구한다
    # 각 점의 값이 폭탄 범위의 step이 된다
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_bomb = 0
    for i in range(n):
        for j in range(m):
            # bomb_area[i][j]가 범위 값이 된다.
            bomb = bomb_area[i][j]

            power = bomb_area[i][j]
            for d in range(4):
                for p in range(1, power + 1):
                    nx = i + dx[d] * p
                    ny = j + dy[d] * p

                    if 0 <= nx < n and 0 <= ny < m:
                        bomb += bomb_area[nx][ny]

                    else:
                        break

            max_bomb = max(max_bomb, bomb)

    print(f"#{test_case} {max_bomb}")
