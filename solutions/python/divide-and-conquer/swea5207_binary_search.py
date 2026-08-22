def binary_search(start, end, target_num, direction):
    global count

    if end < start:
        # 결국 찾지 못한 경우에 대한 처리
        return

    # 중간값을 구한다.
    middle = (start + end) // 2

    if list_a[middle] == target_num:
        count += 1
        return

    elif list_a[middle] < target_num:
        if direction == "R":
            return

        binary_search(middle + 1, end, target_num, "R")

    else:
        if direction == "L":
            return
        binary_search(start, middle - 1, target_num, "L")


T = int(input())

for test_case in range(1, T + 1):
    """
    서로 다른 정수 N개가 주어지면 리스트 A에 저장한다.
    그런 다음 리스트 B에 저장된 정수에 대해 A에 들어있는 수인지 이진 탐색을 진행하려고 한다.
    양쪽구간을 번갈아 선택하는 숫자의 개수에 대해서 알아보려고 한다. => 즉, 오른쪽을 갔으면 반드시 다음번에는 왼쪽을 탐색해야 한다.
    """

    N, M = map(int, input().split())
    list_a = sorted(list(map(int, input().split())))
    list_b = list(map(int, input().split()))

    count = 0
    for b in list_b:
        binary_search(0, N - 1, b, "start")

    print(f"#{test_case} {count}")
