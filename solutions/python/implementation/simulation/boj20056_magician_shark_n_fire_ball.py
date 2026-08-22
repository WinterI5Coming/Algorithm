"""
마법사 상어가 N*N 격자에 파이어볼 M개를 발사했다.
가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. (i번 파이어볼의 위치는 r,c / 질량 m / 방향은 d / 속력은 s 이다)

마법사 상어가 파이어볼에게 이동 명령하면 다음과 같은 일이 발생한다.
    1. 모든 파이어볼이 자신의 방향으로 s만큼 이동한다. (이동 중 여러 파이어볼 존재 가능)
    2. 이동이 모두 끝난 뒤에는 2개 이상의 파이어볼이 존재하는 칸에서는 다음의 일이 일어난다.
        2-1. 모두 하나로 합쳐진다.
        2-2. 파이어볼은 4개로 나누어진다.
        2-3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
            a. 질량은 "합쳐진 파이어볼 질량의 합" / 5
            b. 속력은 "합쳐진 파이어볼 속력의 합" / "합쳐진 파이어볼 개수"
            c. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 => 방향은 (0, 2, 4, 6)
                                                    그렇지 않으면 => 방향은 (1, 3, 5, 7)이 된다.
        2-4. 질량이 0인 파이어볼은 소멸하여 없어진다.
"""

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())
fire_balls = {}

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls[(r - 1, c - 1)] = [(m, d, s)]  # (질량, 방향, 속도)

fire_ball_sum = 0

for _ in range(K):
    # K 번 명령을 했다.

    new_fire_balls = {}
    # 파이어볼의 이동
    for (x, y), fire_ball_list in fire_balls.items():
        for mass, dir_, speed in fire_ball_list:

            # print(x, y, dir_, speed)
            nx = (x + dx[dir_] * speed) % N
            ny = (y + dy[dir_] * speed) % N
            # print(nx, ny)

            if (nx, ny) not in new_fire_balls:
                # 이동한 칸에 파이어볼이 없는 경우
                new_fire_balls[(nx, ny)] = [(mass, dir_, speed)]
            else:
                # 이동한 칸에 파이어볼이 있는 경우
                # => 합체
                new_fire_balls[(nx, ny)].append((mass, dir_, speed))

    # 이제 협쳐진 파이어볼을 확산시켜줘야 한다.
    # 여기서 확산을 하면서 그 과정에서 합쳐진 것들이 존재할 수 있다는 것을 고려해야 한다.
    nxt_fire_balls = {}
    for (x, y), fire_ball_list in new_fire_balls.items():
        if len(fire_ball_list) == 1:
            nxt_fire_balls[(x, y)] = fire_ball_list
            continue

        # 2개 이상의 파이어볼들만 확산을 고려한다.
        fire_ball_cnt, sum_mass, sum_speed = 0, 0, 0
        dir_even, dir_odd = False, False
        for mass, dir_, speed in fire_ball_list:
            fire_ball_cnt += 1
            sum_mass += mass
            sum_speed += speed
            if dir_ % 2 == 0:
                dir_even = True
            else:
                dir_odd = True

        new_mass = sum_mass // 5

        if new_mass != 0:
            nxt_fire_balls[(x, y)] = []

            new_speed = sum_speed // fire_ball_cnt
            # (합쳐진 질량의 합) // 5 가 0이 아닌 경우만을 고려한다.
            # 0이 되면 파이어볼은 사라지기 때문에.
            if dir_even and dir_odd:
                # 방향이 (1, 3, 5, 7)
                for new_dir in (1, 3, 5, 7):
                    nxt_fire_balls[(x, y)].append((new_mass, new_dir, new_speed))

            else:
                # 방향이 (0, 2, 4, 6)
                for new_dir in (0, 2, 4, 6):
                    nxt_fire_balls[(x, y)].append((new_mass, new_dir, new_speed))

    fire_balls = nxt_fire_balls

# print(new_fire_balls)
mass_sum = 0
for fire_ball_list in fire_balls.values():
    for mass, dir_, speed in fire_ball_list:
        mass_sum += mass
print(mass_sum)
