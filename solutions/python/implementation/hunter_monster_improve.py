import sys

sys.setrecursionlimit(10 ** 7)


# sys.stdin = open("input_A2.txt")

def solve_one(n, grid):
    # 1) 값 -> 좌표 저장 (O(1) 조회)
    pos = {}
    monsters = []  # 실제로 존재하는 몬스터 번호들(+k)

    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            if v != 0:
                pos[v] = (i, j)
                if v > 0:
                    monsters.append(v)

    monsters.sort()
    M = len(monsters)

    # 2) "몬스터 번호"가 1..M 연속이 아닐 수도 있으니,
    #    번호 -> 인덱스(0..M-1) 매핑을 만든다.
    idx_of = {m: i for i, m in enumerate(monsters)}

    # 방문 배열
    m_visited = [False] * M  # i번 인덱스 몬스터 방문 여부
    c_visited = [False] * M  # i번 인덱스 고객 방문 여부

    min_time = 10 ** 9

    # 3) DP로 중복 상태 컷 (비트마스크 없이 tuple로)
    # key = (cur_val, tuple(m_visited), tuple(c_visited))
    best = {}

    def dfs(cur_r, cur_c, time, done_m, done_c, cur_val):
        nonlocal min_time

        # 가지치기 1) 이미 최솟값 이상이면 끝
        if time >= min_time:
            return

        # 종료
        if done_m == M and done_c == M:
            min_time = time
            return

        # 가지치기 2) 같은 상태를 더 좋은 시간으로 방문한 적 있으면 컷
        key = (cur_val, tuple(m_visited), tuple(c_visited))
        prev = best.get(key)
        if prev is not None and prev <= time:
            return
        best[key] = time

        # 다음 후보: 몬스터 or 고객
        # (A) 아직 안 잡은 몬스터는 언제든 갈 수 있음
        for m in monsters:
            mi = idx_of[m]
            if m_visited[mi]:
                continue

            nr, nc = pos[m]
            nt = time + abs(nr - cur_r) + abs(nc - cur_c)

            m_visited[mi] = True
            dfs(nr, nc, nt, done_m + 1, done_c, m)
            m_visited[mi] = False

        # (B) 고객은 "해당 몬스터를 잡은 뒤"만 가능
        for m in monsters:
            mi = idx_of[m]
            if not m_visited[mi] or c_visited[mi]:
                continue

            nr, nc = pos[-m]
            nt = time + abs(nr - cur_r) + abs(nc - cur_c)

            c_visited[mi] = True
            dfs(nr, nc, nt, done_m, done_c + 1, -m)
            c_visited[mi] = False

    # 시작: (0,0), time=0, 아무것도 안함
    dfs(0, 0, 0, 0, 0, 0)
    return min_time


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = solve_one(n, grid)

    print(f"#{tc} {ans}")

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