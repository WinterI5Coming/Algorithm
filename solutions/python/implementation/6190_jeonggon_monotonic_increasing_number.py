T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    # num_list의 숫자들에서 두 숫자의 곱하기 조합을 진행한다
    # 각 숫자가 단조 증가하는 수 인지 판단 후
    # 맞다면 최대값을 갱신한다.
    max_result = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            t_num = list(str(num_list[i] * num_list[j]))
            is_increase = True

            # 해당 숫자에 대해서 단조 증가하는 수 인지 검사
            for s in range(len(t_num) - 1):
                if t_num[s] > t_num[s + 1]:
                    is_increase = False
                    break

            if is_increase:
                max_result = max(max_result, num_list[i] * num_list[j])

            else:
                continue
            # print(t_num)
            # print(is_increase)

    print(f"#{test_case} {max_result if max_result != 0 else -1}")