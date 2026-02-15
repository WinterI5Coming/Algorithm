T = int(input())

for test_case in range(1, T+1):
    num_str_len = int(input())
    num_str = input()

    max_cnt = 0
    cnt = 0
    for i in range(num_str_len):
        # 1이 나오기 시작하면 다음도 1인지 0인지 확인
        if num_str[i] == "1":

            # 다음이 1이 나오면
            # => 연속되는 것을 의미하므로 cnt +=1
            cnt += 1

            if i == num_str_len - i or num_str[i+1] == "0":
                # 다음이 0이 나오면
                # => 연속되는 것이 끝나는 것을 의미하므로 max_cnt를 갱신 후 cnt = 0으로 초기화
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                cnt = 0

    print(f"#{test_case} {max_cnt}")