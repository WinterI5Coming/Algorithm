T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 전체는 (1 << 10)
    seen = 0
    total = (1 << 10) - 1 # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     -
    cnt = 0
    while seen != total:
        cnt += 1
        num = N * cnt

        for num_chr in str(num):
            seen |= (1 << int(num_chr))

    print(f"#{test_case} {cnt * N}")
