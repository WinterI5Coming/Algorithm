def is_run(num_arr):
    a, b, c = int(num_arr[0]), int(num_arr[1]), int(num_arr[2])
    return a + 1 == b and b + 1 == c


def is_triplet(num_arr):
    a, b, c = num_arr[0], num_arr[1], num_arr[2]
    return a == b == c


T = int(input())

for test_case in range(1, T + 1):

    # 0 ~ 9 까지 카드6장 뽑았을 때, 3장이 연속적인 경우 run, 3장이 동일한 번호인 경우 triplet이라고 한다
    # 6장의 카드가 run과 triplet으로만 구성된 경우 => baby_gin 이다
    num_list = list(input())
    # 입력받은 숫자카드들로 구성가능한 모든 경우의 수를 만들어본다
    visited = [False] * 6

    # [(현재 선택한 숫자 리스트, 방문한 숫자 카드)]
    stack = [([], visited)]
    is_baby_gin = False
    while stack:
        # print(stack)
        cur_num, v = stack.pop()

        if len(cur_num) < 6:
            for i in range(6):
                if v[i]:
                    continue

                n_v = v[:]
                n_v[i] = True
                stack.append((cur_num + [num_list[i]], n_v))

            continue

        # print(cur_num)
        check_num1 = cur_num[:3]
        check_num2 = cur_num[3:]

        check1 = is_run(check_num1) or is_triplet(check_num1)
        check2 = is_run(check_num2) or is_triplet(check_num2)

        # print(check1, check2)
        if check1 and check2:
            is_baby_gin = True
            break

    print(f"#{test_case} {1 if is_baby_gin else 0}")
