def get_taste(selected_igd):
    taste_list = []

    for a_1 in range(len(selected_igd)):
        visited = [False] * len(selected_igd)
        visited[a_1] = True
        food_1 = selected_igd[a_1]
        for a_2 in range(len(selected_igd)):
            if visited[a_2]:
                continue
            food_2 = selected_igd[a_2]
            # print(food_1, food_2)
            taste_list.append(taste_matrix[food_1][food_2])

    return sum(taste_list)

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    taste_matrix = [list(map(int, input().split())) for _ in range(n)]

    # 두 명의 손님에게 음식 제공, 최대한 비슷한 맛의 음식을 만들어야 한다
    # n개의 식재료 존재하며, 식재료들을 각각 n/2개씩 나누어 두 개의 요리를 진행한다
    # 비슷한 음식이 되기 위해서는 a음식과 b음식의 맛이 최소가 되어야

    igd_list = [i for i in range(n)]
    # 재료 리스트에서 n/2개씩 나누어 준다
    stack = [([], igd_list)]

    min_diff = 99999
    while stack:
        selected_a, remain = stack.pop()

        if len(selected_a) < (n / 2):
            for i in range(len(remain)):

                n_remain = remain[i + 1:]
                stack.append((selected_a + [remain[i]], n_remain))

        elif len(selected_a) == (n / 2):
            selected_b = list(set(igd_list) - set(selected_a))
            # print(selected_a, selected_b)

            # 각 선택 재료에 대한 시너지의 합을 계산해야 한다.
            # selected_a에서 0번째 재료를 고른 경우 선택하지 않은 재료 중에서 하나를 골라야 한다.(순열)
            food_a = get_taste(selected_a)
            food_b = get_taste(selected_b)
            min_diff = min(min_diff, abs(food_a - food_b))

    print(f"#{test_case} {min_diff}")



