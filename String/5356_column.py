T = int(input())

for test_case in range(1, T + 1):
    word_list = [input() for _ in range(5)]
    # 문자열의 각 행의 길이를 구한다
    max_length = max(list(len(w) for w in word_list))

    print(f"#{test_case}", end=" ")
    for j in range(max_length):
        for i in range(5):
            # j번째 idx가 i번째 문자열의 길이보다 크거나 같으면 건너뛰기
            if j >= len(word_list[i]):
                continue
            else:
                print(word_list[i][j], end="")
    print()