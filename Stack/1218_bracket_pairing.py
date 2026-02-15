T = int(input())

for test_case in range(1, T + 1):
    n = int(input())  # 길이
    bracket_str = input()

    bracket_rule = {")": "(", "}": "{", "]": "[", ">": "<"}
    b_stack = []

    for b in bracket_str:

        # stack에 아무것도 없다면 무조건 append()
        if not b_stack:
            b_stack.append(b)
            continue

        # stack에 존재한다면? => 뽑아온 요소가 열린괄호인지 닫힌괄호인지 구분

        # 열린괄호라면 => stack에 넣는다
        if b in bracket_rule.values():
            b_stack.append(b)

        else:
            # 닫힌 괄호라면 = 가장 최근에 넣은 문자열을 가져와서 b의 idx와 비교
            prev_b = b_stack[-1]
            if prev_b == bracket_rule[b]:
                # 이전에 저장된 열린괄호가 지금의 닫힌괄호와 쌍이라면
                # => 스택 pop
                b_stack.pop()

            else:
                # 쌍이 일치하지 않는 경우
                break

    print(b_stack)
    result = 0
    if not b_stack:
        result = 1
    print(f"#{test_case} {result}")
