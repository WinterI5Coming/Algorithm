T = int(input())

for test_case in range(1, T+1):
    a, b = input().split()

    # a 문자열을 순회하면서 b와 같은지 확인한다.
    cnt = 0
    i = 0
    while i < len(a):

        if (len(a) - i) >= len(b) and  a[i] == b[0]:
            # 시작이 같은 경우 => 문자열 전체가 같은지 검사
            # i번째 부터 i + (len(b) - 1)까지의 문자열 검사
            is_same = True
            for j in range(1, len(b)):
                if a[i+j] != b[j]:
                    is_same = False
                    break

            if is_same:
                cnt +=1
                i += len(b)
            else:
                cnt += 1
                i += 1

        else:
            # 아예 다른 경우 => 횟수만 하나 증가
            cnt += 1
            i += 1

    print(f"#{test_case} {cnt}")