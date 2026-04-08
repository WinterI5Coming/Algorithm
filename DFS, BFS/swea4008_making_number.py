"""
N 개의 숫자가 적혀져 있는 게임판이 있고,
    (덧셈, 뺄셈, 곱셈, 나눗셈) 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구하려고 한다.

계산 시에 연산자의 우선 순위는 "고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다."

결과과 최대가 되는 수식과 최소가 되는 수식 찾고, 두 값의 차이를 출력한다.
"""

from collections import deque

T = int(input())

cal_rule = {
    "0": lambda a, b: a + b,
    "1": lambda a, b: a - b,
    "2": lambda a, b: a * b,
    # 파이썬은 (음수 // 양수) 연산의 경우 버림이 아닌 내림 처리가 된다.
    # 따라서 -2 // 3 을 하면 -1 처리가 되고, 이를 방지하기 위해서 다음 같은 처리를 진행했다.
    "3": lambda a, b: int(a / b),
}


def calculator(selected, numbers):
    operation_idx, number_idx = 0, 1
    result = numbers[0]
    while operation_idx < len(selected):
        b, operation = numbers[number_idx], selected[operation_idx]

        result = cal_rule[operation](result, b)
        number_idx += 1
        operation_idx += 1

    return result


def dfs(selected, numbers, operation_list):
    global max_result, min_result
    d = len(selected)

    if d == N - 1:
        # 계산
        result = calculator(selected, numbers)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for i in range(4):
        if operation_list[i] == 0:
            continue

        operation_list[i] -= 1
        dfs(selected + f"{i}", numbers, operation_list)
        operation_list[i] += 1


for test_case in range(1, T + 1):
    N = int(input())
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    INF = float("inf")
    max_result = -INF
    min_result = INF

    dfs("", numbers, operations)
    # print(max_result, min_result)
    print(f"#{test_case} {max_result - min_result}")
