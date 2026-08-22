# T = 10
#
# for test_case in range(1, T + 1):
#     tc = int(input())
#     ladder_matrix = [list(map(int, input().split())) for _ in range(100)]
#
#     # 출발지점을 0행에서 모두 고른다
#     # 각 지점을 순회하면서 도착지점까지의 길이를 구한다
#
#     start_point = [(0, i) for i in range(100) if ladder_matrix[0][i] == 1]
#
#     dy = [-1, 1]
#
#     len_list = []
#     for sx, sy in start_point:
#         # 시작점 sx, sy
#         x, y = sx, sy
#         len_ = 1
#
#         while x < 100:
#             # 먼저 좌우에 길이 있는지 확인한다
#             if 0 <= y - 1 < 100 and ladder_matrix[x][y - 1] == 1:
#                 # 왼쪽에 1이 있는 경우
#                 while 0 <= y - 1 < 100 and ladder_matrix[x][y - 1] == 1:
#                     len_ += 1
#                     y -= 1
#
#             elif 0 <= y + 1 < 100 and ladder_matrix[x][y + 1] == 1:
#                 # 오른쪽에 1이 있는 경우
#                 while 0 <= y + 1 < 100 and ladder_matrix[x][y + 1] == 1:
#                     len_ += 1
#                     y += 1
#
#             x += 1
#             len_ += 1
#
#         len_list.append(len_)
#
#     min_idx = len_list.index(min(len_list))
#     print(f"#{test_case} {start_point[min_idx][1]}")

