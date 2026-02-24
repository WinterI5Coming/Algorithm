N, M = map(int, input().split())  # 3 <=N<= 100, 10<=M<=300,000
card_list = list(map(int, input().split()))

# N장의 card_list에서 3장을 뽑은 합이 M을 넘지 않지만 가장 가까운 합을 구한다
# 조합(combination)

best = 0


def dfs(idx, cnt, cur_sum):
    """
    :param idx: 현재 몇 번 카드까지 봤는지
    :param cnt: 몇 장 골랐는지
    :param cur_sum: 현재까지의 합
    :return: M을 넘지 않는 최대 합
    """
    global best

    if cur_sum > M:
        return

    # 카드 리스트 끝까지 다 돌아본 경우 return
    if idx == N:
        return

    # 3장을 다 고른 경우 best 갱신
    if cnt == 3:
        if cur_sum <= M and cur_sum > best:
            best = cur_sum
            return

    # idx번째의 카드를 고른 경우
    dfs(idx + 1, cnt + 1, cur_sum + card_list[idx])

    # idx번째의 카드를 고르지 않은 경우
    dfs(idx + 1, cnt, cur_sum)

dfs(0, 0, 0)
print(best)