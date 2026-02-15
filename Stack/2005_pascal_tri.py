from pprint import pprint

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    # n * n 의 0으로 가득찬 행렬이 존재한다고 가정
    pascal_tri = [[0 for _ in range(n)] for _ in range(n)]
    # [0][0]에는 무조건 1이 들어간다
    pascal_tri[0][0] = 1

    for i in range(n):
        # i가 0이면 pass
        # i가 1부터 => i행의 i번째 idx까지 숫자를 채운다
        # 숫자를 채울 때는 => 채우고자 하는 위칸 + 그 위칸의 왼쪽 칸 의 합
        if i == 0:
            continue

        for j in range(i + 1):
            # pascal_tri[i][j] 칸을 채운다
            if j == 0:
                # j = 0이면 그 위칸의 값이 그대로 내려온다
                pascal_tri[i][j] = pascal_tri[i-1][j]
            else:
                # j != 0이면 그 위칸 + 그 위칸의 왼쪽칸의 합이 된다
                pascal_tri[i][j] = pascal_tri[i-1][j] + pascal_tri[i-1][j-1]

    # pprint(pascal_tri)
    # 0만을 제거하면서 출력
    print(f"#{test_case}")
    for r in pascal_tri:
        for c in range(len(r)):
            if r[c] != 0:
                print(r[c], end=" ")
        print()
