from pprint import pprint


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    guard_matrix = [list(map(int, input().split())) for _ in range(n)]
    # 1은 기둥 2는 경비병의 위치
    # 경비병은 자신의 위치를 기준으로 n만큼 상하좌우로 관찰이 가능하다
    # 경비병이 탐색 가능한 위치를 3으로 바꾼다
    # 단, 가는 도중 기둥(1)이 존재하는 경우 거기까지

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            val = guard_matrix[i][j]

            if val == 2:
                # 경비병의 경우에 해당 위치를 기준으로 시작
                for d in range(4):
                    # 위치를 기준으로 상하좌우 탐색
                    # 방향을 먼저 정한 뒤 해당 방향으로 1부터 n걸음까지 확인
                    for w in range(1, n + 1):
                        nx = i + dx[d] * w
                        ny = j + dy[d] * w

                        if 0 <= nx < n and 0 <= ny < n:
                            n_val = guard_matrix[nx][ny]
                            if n_val == 1:
                                break
                            else:
                                guard_matrix[nx][ny] = 3

            else:
                continue

    # pprint(guard_matrix)
    cnt = 0
    for p in range(n):
        for q in range(n):
           if guard_matrix[p][q] == 0:
               cnt += 1
    print(f"#{test_case} {cnt}")