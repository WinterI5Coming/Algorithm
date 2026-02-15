T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]


    min_painted = n * m

    # 첫 번째 행은 반드시 하얀색
    # n - 2 까지 흰색이 될 수 있다

    init_cnt = 0
    for w in flag[0]:
        if w != "W":
            init_cnt += 1

    # 스택으로 관리해본다
    # [((a, None), init_cnt, 색칠 끝)]
    flag_stack = [((0, None), init_cnt, 0)]

    while flag_stack:
        (white, blue), paint_cnt, is_painted = flag_stack.pop()

        if blue is None:
            for b in range(white + 1, n - 1):
                flag_stack.append(((white, b), paint_cnt, is_painted))

            if white < n - 2:
                flag_stack.append(((white + 1, None), init_cnt, is_painted))
            continue

        # print(flag_stack)
        # 여기서부터 경우의 수 계산 해본다
        if not is_painted:
            new_paint_cnt = paint_cnt
            # 흰색 ------
            if white != 0:
                for w in range(1, white + 1):
                    for el_w in flag[w]:
                        if el_w != "W":
                            new_paint_cnt += 1

            # 파란색 -----
            for b_r in range(white + 1, blue + 1):
                for el_b in flag[b_r]:
                    if el_b != "B":
                        new_paint_cnt += 1

            # 빨간색 -----
            for r_r in range(blue + 1, n):
                for el_r in flag[r_r]:
                    if el_r != "R":
                        new_paint_cnt += 1

            flag_stack.append(((white, blue), new_paint_cnt, 1))

        else:
             # 여기서는 최소값 갱신한다
            min_painted = min(min_painted, paint_cnt)

    print(f"#{test_case} {min_painted}")

