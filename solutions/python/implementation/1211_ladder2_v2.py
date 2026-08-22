# 새로운 버전
T = 1

for test_case in range(1, T + 1):
    tc = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    # 출발지점을 고른다
    start_point = [i for i in range(100) if ladder_matrix[0][i] == 1]

    # 최소거리 와 최소거리의 x좌표를 설정해 둔다
    best_len = 10 ** 18
    best_y = -1

    # start_point를 순회하면서 거리 측정
    for sy in start_point:
        x, y = 0, sy
        len_ = 1

        while x < 100:

            # 이미 최소거리를 넘은 경우 pass
            if len_ > best_len:
                break

            # 좌우에 대해서 먼저 확인한다
            dy = 0
            if 0 <= y - 1 < 100 and ladder_matrix[x][y - 1]:
                # 왼쪽에 길이 있는 경우
                dy = -1
            elif 0 <= y + 1 < 100 and ladder_matrix[x][y + 1]:
                # 오른쪽에 길이 있는 경우
                dy = 1

            if dy != 0:
                # dy가 0이 아니라면 해당 방향으로 이동해야 한다
                while 0 <= y + dy < 100 and ladder_matrix[x][y + dy] == 1:
                    y += dy
                    len_ += 1

            # dy가 0이라면 아래로만 이동
            x += 1
            len_ += 1

        if best_len >= len_:
            best_len = len_
            best_y = sy

    print(f"#{test_case} {best_y}")
