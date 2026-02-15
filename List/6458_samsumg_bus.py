T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    bus_route = [tuple(map(int, input().split())) for _ in range(n)]  # [(1,3), (2,5)]
    # print(bus_route)

    p = int(input())
    bus_stop_list = [int(input()) for _ in range(p)]

    # 여러 버스 노선이 있고, 각 정류장에서 노선이 몇 개 겹치느냐
    # => 선분의 중첩이 몇 개 있는가?

    # 최대 노선을 먼저 구한다
    bus_line = [0] * 5000

    # 먼저 선분(버스 노선) 겹쳐보기
    for i, j in bus_route:
        # 각 버스 하나의 노선을 가져온다
        start_point, end_point = i - 1, j - 1
        for k in range(start_point, end_point + 1):
            bus_line[k] += 1

    print(f"#{test_case}", end=" ")
    for c in bus_stop_list:
        print(bus_line[c - 1], end=" ")
    print()