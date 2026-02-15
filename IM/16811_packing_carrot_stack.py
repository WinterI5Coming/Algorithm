from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    carrot_list = list(map(int, input().split()))
    carrot_list.sort()

    result = 999999

    limit = n // 2

    # # 사전 불가능 컷(빈도)
    # cnt = defaultdict(int)
    # for x in carrot_list:
    #     cnt[x] += 1
    # if max(cnt.values()) > limit:
    #     print(f"#{test_case} -1")
    #     continue

    # n개 중에서 a개의 당근을 골라 1번 상자에 넣는다

    carrot_stack = [(1, None)]

    while carrot_stack:
        # 스택이 비어있을 때 까지 순회
        box1, box2 = carrot_stack.pop()

        if box2 is None:
            for b in range(box1 + 1, n):
                carrot_stack.append((box1, b))

            if box1 < limit:
                carrot_stack.append((box1 + 1, None))
            continue

        # 여기서 부터는 모든 경우의 수가 확정 되었을 때
        b1, b2, b3 = box1, box2 - box1, n - box2

        # 각 상자가 비어있는 경우
        if b1 <= 0 or b2 <= 0 or b3 <= 0:
            continue

        # limit을 초과한 경우
        if b1 > limit or b2 > limit or b3 > limit:
            continue

        # 같은 값이 다른 상자에 존재하는 경우
        if carrot_list[box1 - 1] == carrot_list[box1]:
            continue
        if carrot_list[box2 - 1] == carrot_list[box2]:
            continue

        diff = max(b1, b2, b3) - min(b1, b2, b3)
        result = min(result, diff)

    print(f"#{test_case} {-1 if result == 999999 else result}")
