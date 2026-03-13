T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    storage = [list(map(int, input().split())) for _ in range(n)]

    # 0은 빈공기 이고 1~9로 된 곳만이 화학물질을 보관하고 있는 곳이다
    # 출력 => 행렬의 개수, 각 행렬의 크기 (크기 작은 순, 크기가 같을 경우 행이 작은 순 출력)

    # storage의 각 점을 순회
    # 0이 아닌 숫자를 만나는 순간 오른쪽과 아래쪽으로 델타 탐색 시작
    # => 가로와 세로 길이를 구한다

    dx = [1, 0]
    dy = [0, 1]

    size = []

    for i in range(n):
        for j in range(n):
            if storage[i][j] != 0:
                row = 1
                col = 1

                for d in range(2):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    while (0 <= nx < n and 0 <= ny < n) and storage[nx][ny] != 0:
                        if d == 0:
                            # 아래쪽 확인
                            row += 1
                            nx += 1
                        else:
                            col += 1
                            ny += 1

                size.append([row, col])
                for p in range(i, i + row):
                    for q in range(j, j + col):
                        storage[p][q] = 0

    # for c in range(len(size) - 1):
    #     for k in range(c + 1, len(size)):
    #         c1 = size[c][0] * size[c][1]
    #         c2 = size[k][0] * size[k][1]
    #
    #         if c1 > c2:
    #             size[c], size[k] = size[k], size[c]
    #
    #         elif c1 == c2:
    #             if size[c][0] > size[k][0]:
    #                 size[c], size[k] = size[k], size[c]

    size.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f"#{test_case}", end=" ")
    print(len(size), end=" ")
    for s in size:
        print(*s, end=" ")
    print()
