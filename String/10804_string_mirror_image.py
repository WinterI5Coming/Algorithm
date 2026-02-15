T = int(input())

for test_case in range(1, T+1):
    target_str = input()

    # "bdppq" => 먼저 순서 뒤집기 => "qppdb" => 서로 맞는 쌍에 대해 반대로 적용 => "pqqbd"

    mirror_rule = {"p": "q", "q": "p", "b": "d", "d": "b"}
    mirror_str = ""
    for w in target_str:
        mirror_str = mirror_rule[w] + mirror_str

    print(f"#{test_case} {mirror_str}")
