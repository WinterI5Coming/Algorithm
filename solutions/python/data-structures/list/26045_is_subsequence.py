T = int(input())

for test_case in range(1, T + 1):
    len_a, len_b = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    is_subsequence = True

    idx = 0
    for el_b in list_b:
        list_a = list_a[idx:]

        if el_b in list_a:
            idx = list_a.index(el_b) + 1

        else:
            is_subsequence = False
            break

    if is_subsequence:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
