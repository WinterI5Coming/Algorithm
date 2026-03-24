N, K = map(int, input().split())
coin_type = [int(input()) for _ in range(N)]

target = K
idx = N - 1

coin_cnt = 0
while target > 0:

    if (target // coin_type[idx]) > 0:

        coin_cnt += target // coin_type[idx]
        target -= coin_type[idx] * (target // coin_type[idx])

    else:
        idx -= 1

print(coin_cnt)