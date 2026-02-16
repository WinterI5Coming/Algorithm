T = 1

for test_case in range(1, T+1):
    tc = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    # 출발지점을 0행에서 모두 고른다
    # 각 지점을 순회하면서 도착지점까지의 길이를 구한다

    start_point = [(0,i) for i in range(100) if ladder_matrix[0][i] == 1]

    dy = [-1, 1]

    len_list = []
    for sx, sy in start_point:
        # 시작점 sx, sy
        x, y = sx, sy
        len_ = 1

        while x < 100:
            # 먼저 좌우에 길이 있는지 확인한다
            for d in range(2):
                ny = y + dy[d]

                if 0 <= ny < 100:
                    if ladder_matrix[x][ny] != 1:

                        # 좌우에 길이 있다면 => 0을 만날 때 까지 그 방향으로 이동
                    print(ladder_matrix[x][ny])
                    while ladder_matrix[x][ny] == 1:
                        len_ += 1
                        ny += dy[d]
                    y = ny - dy[d]
                    break

            x += 1
            len_ += 1

        len_list.append(len_)

    print(f"#{test_case}")
    print(*len_list)





