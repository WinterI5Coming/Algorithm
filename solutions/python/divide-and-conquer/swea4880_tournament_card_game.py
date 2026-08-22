def play_game(player_1, player_2):
    p1_card_idx, p2_card_idx = player_1[0] - 1, player_2[0] - 1
    p1_card, p2_card = card_num[p1_card_idx], card_num[p2_card_idx]
    card_sum = p1_card + p2_card

    if p1_card == p2_card:
        return player_1

    if card_sum == 3:
        return player_1 if p1_card == 2 else player_2
    elif card_sum == 4:
        return player_1 if p1_card == 1 else player_2
    else:
        return player_1 if p1_card == 3 else player_2


def tournament_game(arr):
    if len(arr) == 1:
        return arr

    middle = (0 + (len(arr) - 1)) // 2
    left_half = arr[:middle + 1]
    right_half = arr[middle + 1:]

    player_1 = tournament_game(left_half)
    player_2 = tournament_game(right_half)

    return play_game(player_1, player_2)


T = int(input())

for test_case in range(1, T + 1):
    """
    가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는다.
    N명의 사람이 N장의 카드를 나눠 갖은 후, 그룹을 나누게 된다.
    
    가위바위보 룰은 다음과 같이 한다.
    1 + 2 => 2 / 가위 바위 => 바위
    1 + 3 => 1 / 가위 보 => 가위
    2 + 3 => 3 / 바위 보 => 보
    """

    N = int(input())  # 인원수
    card_num = list(map(int, input().split()))
    player = list(range(1, N + 1))

    winner = tournament_game(player)
    print(f"#{test_case}", end=" ")
    print(*winner)
