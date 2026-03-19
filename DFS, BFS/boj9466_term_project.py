# ------------------------------------------------------------------------
# [함수형 그래프(Functional Graph) + DFS (사이클)]
import sys

sys.setrecursionlimit(10 ** 9)

T = int(input())


def dfs(x):
    global team_cnt

    visited[x] = True  # 방문 처리
    nxt = stu_choose[x]  # x 학생이 지목한 다음 학생

    if not visited[nxt]:
        # 다음 학생을 방문하지 않았다면 계속 DFS 진행
        dfs(nxt)

    else:
        # 지목한 학생을 이미 방문한 경우
        # 즉, 1 -> 3 -> 3 이런식으로 가던 중 방문했던 학생을 또 다시 만난 경우
        # => 사이클인지를 확인해야 한다.

        """
        해당 문제의 DFS 에서 노드는 3가지 상태로 존재한다:
            1. 아직 안 감 => visited = False
            2. 지금 탐색 중 => visited = True, finished = False
            3. 탐색 완료 => visited = True, finished = True
        
        현재 else 문에서 보고자 하는 것은 지금 탐색 중인 경로(DFS)안에 있느냐?
        DFS 는 다음과 같이 움직인다 : 1 -> 2 -> 3 -> 4 -> 5 하나의 줄처럼
            여기서 3을 "다시" 만난다면,
            이건 반드시 루프, 사이클이다.
            반대로 이미 끝난 3을 다시 만난다면 그건 다른 DFS 에서 만든거지 우리랑은 관계 없는 것이다.
        """

        if not finished[nxt]:
            cur = nxt  # 마지막에 나온 중복 방문된 학생을 cur 에 저장
            cnt = 1  # 중복된 경우가 이미 나온 것이기 때문에 팀에 한 명은 확보된 것이나 마찬가지

            # 다시 거슬러 올라가서 cur이 지목한 학생이 있는지를 확인하는 과정
            # 6(x) -> 4(nxt, cur) 인 경우 거슬러 올라가서 4는 누굴 지목했는지 확인한다.
            # 4 -> 7(cur) (cnt += 1) => 7 -> 6(cur) (cnt += 1) => x = cur 이므로 탈출
            while cur != x:
                cur = stu_choose[cur]
                cnt += 1

            team_cnt += cnt

    # 작업 완료 처리를 왜 else 문 안에서 하지 않느냐?
    # => else 문 안에 있으면 위의 첫 if 문에서 들어간 x들이 작업 완료 처리가 되지 않는다.
    # 즉, x를 시작으로 한 DFS 가 처리가 모두 끝났음을 표시
    finished[x] = True


for test_case in range(1, T + 1):
    N = int(input())
    stu_choose = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)  # 방문했는지 확인하는 리스트
    finished = [False] * (N + 1)  # 작업을 완료했는지를 확인하는 리스트
    team_cnt = 0

    for i in range(1, N + 1):

        if not visited[i]:
            dfs(i)

    print(N - team_cnt)

# ------------------------------------------------------------------------
# [위상정렬]
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    stu_choose = [0] + list(map(int, input().split()))

    in_degree = [0] * (N + 1)
    for i in range(1, N + 1):
        nxt = stu_choose[i]
        in_degree[nxt] += 1

    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()

        nxt = stu_choose[x]
        in_degree[nxt] -= 1

        if in_degree[nxt] == 0:
            q.append(nxt)

    # print(in_degree)
    print(in_degree.count(0) - 1)

# ------------------------------------------------------------------------
# [시간초과로 인한 실패...]
# T = int(input())
#
# for test_case in range(1, T + 1):
#     """
#     텀 프로젝트를 수행해야 하며, 프로젝트 팀원 수에는 제한이 없다.
#     심지어 모든 학생들이 동일한 팀의 팀원인 경우 한 팀만 존재할 수도 있다.
#     모든 학생들은 함께 프로젝트를 하고 싶은 학생을 선택해야 한다.(단, 한 명만 선택할 수 있고 혼자 하고 싶은 경우 본인 선택도 가능하다.)
#
#     어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산한다.
#     """
#     N = int(input())
#     stu_choose = [0] + list(map(int, input().split()))
#
#     result = [False] * (N + 1)
#     for i in range(1, N + 1):
#         visited = [False] * (N + 1)
#         path = [i]
#
#         cur = i
#         while True:
#             if not visited[stu_choose[cur]]:
#                 visited[stu_choose[cur]] = True
#                 path.append(stu_choose[cur])
#                 cur = stu_choose[cur]
#             else:
#                 break
#
#         if path[0] == path[-1]:
#             for p in path:
#                 if not result[p]:
#                     result[p] = True
#         # print(path)
#
#     print(result.count(False) - 1)
