T = int(input())

for test_case in range(1, T + 1):
    """
    암호코드는 8개의 숫자로 이루어져 있다.
    암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어진다.
        따라서 암호코드의 길이는 56이다.
    올바른 암호코드는 (홀수 자리의 합 * 3) + (짝수 자리의 합)이 10의 배수가 되야한다.
    """
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    rule = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9
    }

    target_pw = ""
    for row in matrix:
        if "1" in row:
            for i in range(M - 1, 0, -1):
                if row[i] == "1":
                    target_pw = row[i - 55:i + 1]
                    break

            break

    odd_sum = 0
    even_sum = 0

    for j in range(8):
        # 0 6 / 7 13 / 14 20 ...
        start, end = j * 7, j * 7 + 7
        target = target_pw[start: end]
        # print("".join(target))
        key = "".join(target)
        # print(rule[key])

        # j를 2로 나누었을 때 나머지가 0이면 홀수자리, 1이면 짝수자리\
        if j % 2 == 0:
            odd_sum += rule[key]
        else:
            even_sum += rule[key]

    result = odd_sum + even_sum if (odd_sum * 3 + even_sum) % 10 == 0 else 0
    print(f"#{test_case} {result}")
