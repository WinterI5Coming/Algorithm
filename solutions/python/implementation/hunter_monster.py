"""
[문제 복원 - 몬스터 & 고객 최소 이동 시간]

1. 격자 정보
- N x N 크기의 2차원 배열
- 각 칸의 값 의미:
    0   : 빈 칸
    k   : k번 몬스터 (k > 0)
   -k   : k번 고객(사람)

2. 시작 위치
- 헌터는 (0, 0)에서 시작

3. 이동 규칙
- 상하좌우 이동 가능
- 장애물은 없음 (숫자는 위치 표시용)

4. 반드시 지켜야 할 제약
- k번 고객(-k)은 반드시
  k번 몬스터(k)를 먼저 처치한 뒤에만 방문 가능

5. 목표
- 모든 몬스터를 처치하고
- 모든 고객을 방문했을 때
- 총 이동 시간의 최소값을 구하라
"""
def cal_time(route):
    # route로 순서를 받았으니 각 값에 대한 좌표가 필요하다
    cur_pos = [0, 0]
    time = 0
    for r in range(len(route)):

        nxt_pos =  [[p, q] for p in range(n) for q in range(n) if map_[p][q] == route[r]]
        time += abs(nxt_pos[0][0] - cur_pos[0])  + abs(nxt_pos[0][1] - cur_pos[1])

        if time > min_time:
            return False

        cur_pos = nxt_pos[0]

    return time


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    map_ = [list(map(int, input().split())) for _ in range(n)]

    monster_spot = [map_[i][j] for i in range(n) for j in range(n) if map_[i][j] > 0]
    customer_spot = [map_[i][j] for i in range(n) for j in range(n) if map_[i][j] < 0]

    total_spot = monster_spot + customer_spot
    t_cnt = len(total_spot)
    # print(total_spot)

    visited = [False] * len(total_spot)
    stack = [([], visited)]

    min_time = 9999
    while stack:
        finished, visit = stack.pop()

        if not finished:
            # 처음 시작할 때는 몬스터를 하나 잡아야 한다
            for i in range(t_cnt):
                if visit[i] or total_spot[i] < 0:
                    continue

                init_visit = visit[:]
                init_visit[i] = True
                stack.append((finished + [total_spot[i]], init_visit))
            continue

        elif len(finished) < t_cnt:
            for j in range(t_cnt):
                if visit[j]:
                    continue
                if total_spot[j] < 0 and -total_spot[j] not in finished:
                    continue

                n_visit = visit[:]
                n_visit[j] = True
                stack.append((finished + [total_spot[j]], n_visit))

        elif len(finished) == t_cnt:
            finished_time = cal_time(finished)

            if not finished_time:
                continue
            min_time = min(min_time, finished_time)

    print(f"#{test_case} {min_time}")
"""
5
3
0 0 0
0 1 -1
0 0 0
4
-3 -1 1 0
-2 0 0 3
0 0 0 0
0 0 2 0
5
0 0 -3 0 0
0 0 0 3 0
0 0 0 0 2
0 0 1 0 0
-1 0 0 -2 0
6
-1 0 0 0 0 -4
0 0 0 0 2 0
-3 -2 0 4 0 0
3 0 0 0 0 1
0 0 0 0 0 0
0 0 0 0 0 0
8
3 0 0 0 -2 0 0 0
0 0 0 0 -4 0 0 0
0 0 0 0 0 0 0 0
0 0 -1 0 0 0 0 0
0 -3 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 2 4 0 1 0 0
0 0 0 0 0 0 0 0

# output
3
13
18
22
22
"""
