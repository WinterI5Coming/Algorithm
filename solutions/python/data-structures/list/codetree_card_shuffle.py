N = int(input())
card_list = list(map(int, input().split()))

"""
전체 카드 더미를 절반씩 나눈다.
나눈 카드 더미 중 왼쪽 더미의 맨 위 카드와 오른쪽 더미의 맨 위 카드에 적인 수의 합을 확인하여 새로운 카드 더미를 만든다.
    => 합이 홀수이면, 왼쪽 더미의 맨 위 카드를 뽑는다
    => 합이 짝수이면, 오른쪽 더미의 맨 위 카드를 뽑는다
한쪽 더미가 모두 비게 되면, 남은 더미에 있는 카드들을 순서대로 새로운 더미 뒤에 붙인다.

[1 2 3] [4 5 6]
=> 1 + 4 = 홀수, [1]
=> 2 + 4 = 짝수, [1, 4]
=> 2 + 5 = 홀수, [1, 4, 2]
=> 3 + 5 = 짝수, [1, 4, 2, 5]
=> 3 + 6 = 홀수, [1, 4, 2, 5, 3]
=> 왼쪽 카드 더미가 다 비었으므로, [1, 4, 2, 5, 3] + [6]
"""

mid = int(N / 2)
i, j = 0, mid

n_card_list = []
while i < mid and j < N:
    a, b = card_list[i], card_list[j]

    if (a + b) % 2 == 0:
        n_card_list.append(b)
        j += 1
    else:
        n_card_list.append(a)
        i += 1

# print(i, j)

if i == mid:
    n_card_list += card_list[j:]
else:
    n_card_list += card_list[i:mid]
print(*n_card_list)
