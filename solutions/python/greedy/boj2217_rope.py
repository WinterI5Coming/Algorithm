"""
N(최대 10^5)개의 로프가 주어진다. 각각의 로프는 버틸 수 있는 최대 중량이 존재한다.
    단, 여러 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
    k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 w/k만큼의 중량이 걸린다.

로프를 이용하여 들어올릴 수 있는 물체의 최대 중량을 구한다.


3 4 7 14 15 20 의 로프가 존재한다.
1) max = 20
2) 이제 여러 개를 선택할 수 있다.


"""

N = int(input())
rope = sorted([int(input()) for _ in range(N)])
# print(rope)


best = 0
for i in range(N):
    best = max(best, rope[i] * (N - i))

print(best)
