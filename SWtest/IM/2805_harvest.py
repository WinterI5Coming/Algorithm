from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    farm_matrix = [list(map(int, input())) for _ in range(n)]
    # pprint(farm_matrix)

    # 농장의 크기는 반드시 홀수
    # 수확은 항상 농장의 크기에 따른 정사각형 마름모 형태로만 가능

    mid = n // 2
    harvest_sum = sum(farm_matrix[mid])

    # 가운데 행은 반드시 모두 포함
    # 상, 하로 행을 이동하는 경우 -2씩 진행
    # 즉, 행을 기준으로 상하로 이동 한다고 생각한다

    # farm_matrix[mid][mid]
    dx = [-1, 1]
    for d in range(2):
        for w in range(1, n - mid):
            nx = mid + dx[d] * w

            # farm_matrix[nx]의 행을 (0 + w) ~ (n - w)
            for k in range(0 + w, n - w):
                # print(k)
                harvest_sum += farm_matrix[nx][k]

    print(f"#{test_case} {harvest_sum}")
