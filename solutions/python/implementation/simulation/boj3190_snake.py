"""
N*N 보드 위에서 뱀이 기어다닌다.
    사과를 먹으면 뱀 길이가 늘어나고, 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임이 시작할 때 맨위 맨좌측에 위치하고 뱀의 길이는 1이다. 처음에 오른쪽을 향한다.
    1) 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    2) 만약 벽이나 자기자신의 몸과 부딪히면 끝이다.
    3) 이동한 칸에 사과가 있으면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다. (= 길이가 1늘어난다.)
    4) 이동한 칸에 사과가 없으면, 몸길이를 줄여 꼬리가 위치한 칸을 비워준다.

게임이 몇 초에 끝나는가?
"""

from collections import deque


N = int(input())
K = int(input())  # 사과의 개수

# 사과는 set으로 저장한다.
apple = set()
for _ in range(K):
    x, y = map(int, input().split())
    apple.add((x - 1, y - 1))

L = int(input())
commands = [
    (int(sec_com), dir_com)
    for sec_com, dir_com in [tuple(input().split()) for _ in range(L)]
]

turn_rule = {
    0: {"L": 3, "D": 1},
    1: {"L": 0, "D": 2},
    2: {"L": 1, "D": 3},
    3: {"L": 2, "D": 0},
}
# 우하좌상
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 큐 자체를 뱀이라고 생각하고 구현한다.
# 시간이 흘러감에 따라
#   1. 머리가 먼저 이동한다. => 머리를 꺼내온다.
#   2. 머리가 이동한 칸이 충돌하지 않았는지 확인한다.
#       2-1. 충돌한 경우 => 즉시 종료
#       2-2. 충돌하지 않은 경우 => 사과가 존재하는지 확인한다.
#   3. 사과가 존재한다면 => apple에 있는 해당 사과 삭제 + 새로운 머리 큐에 넣어주기
#       3-1. 사과가 존재하지 않는다면 => pass
#   4. 시간의 흐름에 따라 방향전환을 정해진 규칙에 맞게 해주어야 한다.
snake = deque([(0, 0)])
direction = 0
cmd_idx = 0

time = 0
while snake:
    time += 1

    hx, hy = snake[-1]
    n_hx, n_hy = hx + dx[direction], hy + dy[direction]

    if not (0 <= n_hx < N and 0 <= n_hy < N):
        break

    tail = snake[0]

    if (n_hx, n_hy) in snake:
        break

    snake.append((n_hx, n_hy))

    if (n_hx, n_hy) in apple:
        apple.remove((n_hx, n_hy))
    else:
        tx, ty = snake.popleft()

    if cmd_idx < L and time == commands[cmd_idx][0]:
        _, cmd_dir = commands[cmd_idx]
        direction = turn_rule[direction][cmd_dir]
        cmd_idx += 1

print(time)
