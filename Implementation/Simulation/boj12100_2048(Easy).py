"""
상하좌우 네 방향 중 하나로 이동시키는 것이 가능하다. 이때, 같은 값을 갖는 두 블록이 충돌하면 하나로 합쳐지게 된다.
    단, 한 번의 이동에서 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
    또, 똑같은 수가 세 개가 있는 경우에느 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.

일단 상하좌우 방향에 대해 정의한다. => 0, 1, 2, 3 (상, 하, 좌, 우)
    1) 상 => 각 열을 위에서부터 (= 0행부터) 차례대로 가져온다.
    2) 하 => 각 열을 아래서부터 (= N-1 행부터) 차례대로 가져온다.
    3) 좌 => 각 행을 왼쪽에서부터 (= 0열부터) 차례대로 가져온다.
    4) 우 => 각 행을 오른쪽에서부터 (= N-1열부터) 차례대로 가져온다.

! 해당 방법으로는 불가
예를 들어, [2, 4, 4, 8, 2, 2] 로 가져온 경우
   i번 인덱스 부터 순회를 시작함과 동시에 i+1번째 인덱스를 가져와 동일한 값인지를 확인한다.
      => 동일한 값인 경우에는 => 합쳐준다.
                                  => 두 값을 합친 뒤에 [0:i] + [더한 값] + [i+2:] + [0] 으로 합쳐준다.
       => 동일하지 않은 경우에는 => 다음 인덱스로 continue

* 다음의 방법을 적용해야 한다.
2048은 인접 값 비교로 처리할 수 없고,
"압축 → 병합 → 패딩" 순서로 처리해야 한다.

- 압축: 0 제거
- 병합: 앞에서부터 같은 값 1회만 합치기 (i += 2)
- 패딩: 남은 자리에 0 채우기
"""

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def sweep(direction, new_board):

    if direction <= 1:
        # 상하의 경우 => 열 가져오기

        if direction == 0:
            for col in range(N):
                target = []
                for row in range(N):

                    if new_board[row][col] != 0:
                        target.append(new_board[row][col])

                # 여기서 모아놓은 한 열에 대한 처리 진행한다.
                i = 0
                merged = []
                while i < len(target):
                    if i + 1 < len(target) and target[i] == target[i + 1]:
                        v = target[i] * 2
                        merged.append(v)
                        i += 2
                    else:
                        merged.append(target[i])
                        i += 1

                merged += [0] * (N - len(merged))

                # 이제는 이 target을 어떻게 반영해 줄 것인지 + 그리고 어떻게 백트래킹으로 되돌릴 것인지
                for row in range(N):
                    new_board[row][col] = merged[row]

        else:
            for col in range(N):
                target = []
                for row in range(N - 1, -1, -1):

                    if new_board[row][col] != 0:
                        target.append(new_board[row][col])

                # 여기서 모아놓은 한 열에 대한 처리 진행한다.
                i = 0
                merged = []
                while i < len(target):
                    if i + 1 < len(target) and target[i] == target[i + 1]:
                        v = target[i] * 2
                        merged.append(v)
                        i += 2
                    else:
                        merged.append(target[i])
                        i += 1

                merged += [0] * (N - len(merged))

                # 이제는 이 target을 어떻게 반영해 줄 것인지 + 그리고 어떻게 백트래킹으로 되돌릴 것인지
                for row in range(N - 1, -1, -1):
                    new_board[row][col] = merged[N - 1 - row]

    else:
        # 좌우의 경우 => 행 가져오기

        if direction == 2:

            for row in range(N):
                target = []
                for col in range(N):

                    if new_board[row][col] != 0:
                        target.append(new_board[row][col])

                i = 0
                merged = []
                while i < len(target):
                    if i + 1 < len(target) and target[i] == target[i + 1]:
                        v = target[i] * 2
                        merged.append(v)
                        i += 2
                    else:
                        merged.append(target[i])
                        i += 1

                merged += [0] * (N - len(merged))

                for col in range(N):
                    new_board[row][col] = merged[col]

        else:

            for row in range(N):
                target = []
                for col in range(N - 1, -1, -1):

                    if new_board[row][col] != 0:
                        target.append(new_board[row][col])

                i = 0
                merged = []
                while i < len(target):
                    if i + 1 < len(target) and target[i] == target[i + 1]:
                        v = target[i] * 2
                        merged.append(v)
                        i += 2
                    else:
                        merged.append(target[i])
                        i += 1

                merged += [0] * (N - len(merged))

                for col in range(N - 1, -1, -1):
                    new_board[row][col] = merged[N - 1 - col]


def get_max_size(board):
    m_size = 0
    for row in board:
        m_size = max(m_size, max(row))

    return m_size


# 5번의 이동 동안 4방향을 모두 고려해야 한다.
max_size = 0


def dfs(cnt, b):
    global max_size

    # 종료 조건
    if cnt == 5:
        max_size = max(max_size, get_max_size(b))

        return

    for d in range(4):
        # d 방향으로 움직이기를 정한다.

        new_board = [row[:] for row in b]
        sweep(d, new_board)
        dfs(cnt + 1, new_board)


dfs(0, board)
print(max_size)
