"""
8개의 톱니를 가지고 있는 톱니바퀴 4개가 일렬로 존재한다.

톱니바퀴를 K번 회전시키려고 하는데, 시계방향과 반시계방향이 존재한다.
    이때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고 회전시키지 않을 수도 있다.
            => 맞닿은 극이 다르다면 => A가 회전한 방향과 반대방향으로 회전한다.
            => 맞닿은 극이 같다면 => 회전하지않는다.
"""


def right_dir_search(gear_idx, gears, gears_dir):
    for i in range(gear_idx + 1, 4):
        if gears[i - 1][2] != gears[i][6]:
            gears_dir[i] = -gears_dir[i - 1]
        else:
            # 극이 같게 되면 즉시 멈춘다.
            break


def left_dir_search(gear_idx, gears, gears_dir):
    for i in range(gear_idx - 1, -1, -1):
        if gears[i + 1][6] != gears[i][2]:
            gears_dir[i] = -gears_dir[i + 1]
        else:
            # 극이 같게 되면 즉시 멈춘다.
            break


def main():
    gears = [list(input()) for _ in range(4)]
    K = int(input())
    commands = [
        (i - 1, j) for i, j in [tuple(map(int, input().split())) for _ in range(K)]
    ]

    for gear_idx, dir_ in commands:

        gears_dir = [0, 0, 0, 0]
        gears_dir[gear_idx] = dir_

        right_dir_search(gear_idx, gears, gears_dir)
        left_dir_search(gear_idx, gears, gears_dir)

        new_gears = []
        for i in range(4):
            gear_dir = gears_dir[i]
            old_gear = gears[i]
            if gear_dir == 0:
                new_gear = old_gear

            elif gear_dir == -1:
                # 반시계 방향
                new_gear = old_gear[1:8] + [old_gear[0]]
            else:
                # 시계 방향
                new_gear = [old_gear[7]] + old_gear[0:7]

            new_gears.append(new_gear)
        gears = new_gears

    result = 0
    for i in range(4):
        if gears[i][0] == "1":
            result += 2**i
    print(result)


main()
