T = int(input())


def binary_search_recur(start_page, end_page, target):
    count = 0

    count += 1
    middle = (start_page + end_page) // 2  # 중간값 계산
    if middle == target:
        # 목표를 찾은 경우
        return count

    elif middle > target:
        # 목표가 더 작은 경우
        count += binary_search_recur(start_page, middle, target)

    else:
        # 목표가 더 큰 경우
        count += binary_search_recur(middle, end_page, target)

    return count


def binary_search(end_page, target):
    start = 1
    end = end_page
    count = 0

    # 시작점이 끝점보다 작거나 같은 동안 계속 탐색
    while start <= end:

        count += 1  # 탐색 횟수 증가

        mid = (start + end) // 2  # 중간값 계산

        if mid == target:
            # 목표를 찾은 경우
            return count

        elif mid > target:
            # 목표가 중간값보다 작은 경우
            # => 중간값을 끝점으로 설정하고 다시 탐색
            end = mid
        else:
            # 목표가 중간값보다 큰 경우
            # => 중간값을 시작점으로 설정하고 다시 탐색
            start = mid

    return count


for test_case in range(1, T + 1):
    P, p_a, p_b = map(int, input().split())

    # count_a = binary_search(P, p_a)
    # count_b = binary_search(P, p_b)
    count_a = binary_search_recur(1, P, p_a)
    count_b = binary_search_recur(1, P, p_b)

    winner = ""
    if count_a < count_b:
        winner = "A"
    elif count_a > count_b:
        winner = "B"
    else:
        winner = "0"

    print(f"#{test_case} {winner}")
