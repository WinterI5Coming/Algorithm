T = int(input())

for test_case in range(1, T + 1):

    """
    3장부터 서로 나눠주기 시작한다.
    
        1) 먼저 triplet에 대해서 검사
        2) triplet이 되지 않은 경우, run을 검사 하기 위해 조합을 만든다
    """


    def chk_triplet(cards):

        for n in cards:
            if cards.count(n) >= 3:
                return True

        return False


    def chk_run(cards):

        # 카드를 오름차순으로 정렬 후, set을 사용하여 중복을 제거한다
        cards_set = set(cards)
        cards_list = list(cards_set)
        cards_list.sort()
        if len(cards_set) < 3:
            return False

        for n in range(len(cards_set) - 2):
            if cards_list[n] + 1 == cards_list[n + 1] and cards_list[n + 1] + 1 == cards_list[n + 2]:
                return True

        return False


    nums = list(map(int, input().split()))
    p1, p2 = [], []
    for cnt in range(6):
        p1.append(nums[2 * cnt])
        p2.append(nums[2 * cnt + 1])
    # print(p1, p2)

    result = 0
    for i in range(4):
        player_1, player_2 = p1[:3 + i], p2[:3 + i]

        p1_win = chk_triplet(player_1) or chk_run(player_1)
        p2_win = chk_triplet(player_2) or chk_run(player_2)

        if p1_win or p2_win:
            result = 1 if p1_win else 2
            break
        elif p1_win and p2_win:
            result = 1
            break

    print(f"#{test_case} {result}")
