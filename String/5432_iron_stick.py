T = int(input())

for test_case in range(1, T+1):
    s = input()
    """
    ()(((()())(())()))(())    
    """

    laser = 0
    laser_stack = []
    result = 0
    i = 0

    while i < len(s):
        if s[i] == "(":
            # 괄호가 열리는 경우
            if i + 1 < n and s[i + 1] == ")":
                # => 다음에 바로 닫히거나
                # 바로 닫히면 레이져이기 때문에 laser += 1 + 다음 칸 건너뛰기
                laser += 1
                i += 2

            else:
                # => 다음에도 다시 열리거나
                # 다음에도 다시 괄호가 열린다는 것은 지금의 "열린 괄호"는 파이프 라는 것을 의미
                # 해당 파이프 이전의 레이저 수를 저장
                laser_stack.append(laser)

        else:
            # 괄호가 닫히는 경우
            # 전체 레이저 수 - 가장 최근에 laser_stack에 들어간 레이저 수(해당 파이프 이전에 존재하는 레이저 수)
            # = 해당 파이프에만 관여하고 있는 레이저 수
            start_laser = laser_stack.pop()
            result = (laser - start_laser) + 1

        i += 1

    print(f"#{test_case} {result}")


