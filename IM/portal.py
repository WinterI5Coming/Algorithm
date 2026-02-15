import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    room_n = int(input()) # 방의 수 5
    room_list = list(map(int, input().split())) # 방 리스트 [0, 1, 1, 2, 0]
    visited = [False] * room_n

    portal_cnt = 0
    cur = 0 # 현재 위치 idx
    while cur < room_n - 1:

        if cur == 0:
            # 현재 위치가 첫 방(0)이면 다음 방으로 이동
            visited[cur] = True
            cur += 1
            portal_cnt += 1

        else:
            # 다음 방의 경우에는 방문 여부에 따라 달라진다
            if not visited[cur]:
                # 첫 방문의 경우 => (해당 방의 값 - 1) idx로 이동
                visited[cur] = True
                cur = room_list[cur] - 1
                portal_cnt += 1

            else:
                # 이미 방문을 했던 경우 => 다음 방 이동
                cur += 1
                portal_cnt += 1

    print(f"#{test_case} {portal_cnt}")



