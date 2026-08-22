# N개의 당근을 주문하면 => 대, 중, 소로 구분하여 포장
# 조건)
# 1. 같은 크기의 당근은 같은 상자에 있어야 하고 + 빈상자는 존재 X
# 2. 한 상자에 N/2개를 초과하는 당근이 있을 수 없다 (N이 홀수이면 소수점 버림) ex. N=7이면 3개 초과 불가
# => 해당 조건을 만족하면서 각 상자의 당근 개수 차이가 최소가 되도록 포장
from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())  # 당근의 개수
    carrot_list = list(map(int, input().split()))  # [1, 2, 3, 4, 5, 6, 7, 8]
    carrot_list.sort()

    can_package = True

    # 세 개의 상자에 최소 N/2개는 들어가야 함
    carrot_limit = n // 2  # 한 상제 넘어서는 안되느니 최대값

    # 1. 같은 숫자가 carrot_limit을 넘어서는 수만큼 있는 경우 불가
    carrot_cnt = defaultdict(int)
    for el in carrot_list:
        carrot_cnt[el] += 1

    for i in carrot_cnt.values():
        if i > carrot_limit:
            can_package = False
            break

    best = 1000

    # 첫 상자에 들어갈 당근을 골라본다 (최소 1개부터 최대 carrot_limit개 까지 고르기 가능)
    for a in range(1, carrot_limit + 1):
        # a개를 골라 1번 상자에 넣는다
        is_done = True
        for b in range(1, min(carrot_limit, n - a - 1) + 1):
            # b개를 골라 2번 상자에 넣는다
            # 3번 상자에는 n - a - b개가 들어가게 된다
            box1 = carrot_list[:a]
            box2 = carrot_list[a:a + b]
            box3 = carrot_list[a + b:]
         # print(carrot_box)
         # 빈 상자 방지
            if not box1 or not box2 or not box3:
                continue
         # 각 상자 크기 제한
            if len(box1) > carrot_limit or len(box2) > carrot_limit or len(box3) > carrot_limit:
                continue
         # 같은 숫자가 서로 다른 상자에 들어간 경우 pass
            # [1, 1, 1] [1, 2, 2, 2] [3]
            # 즉, 교집합이 없어야 한다
            s1, s2, s3 = set(box1), set(box2), set(box3)
            if (s1 & s2) or (s1 & s3) or (s2 & s3):
                continue

            sizes = [len(box1), len(box2), len(box3)]
            # print(f"#{test_case} {max(sizes) - min(sizes)}")
            diff = max(sizes) - min(sizes)
            best = min(best, diff)

    print(f"#{test_case} {-1 if best == 1000 else best}")




