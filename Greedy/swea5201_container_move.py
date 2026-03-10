T = int(input())

for test_case in range(1, T + 1):

    """
    트럭당 한 개의 컨테이너 운반 가능하고, 적재용량 초과하는 컨테이너는 운반 불가하다.
    최대 M대의 트럭이 편도로 한번 운행한다.
    화물의 총 중량이 최대가 되도록 옮길 때, 옮겨진 전체 문게가 얼마인지 출력한다.
    
    먼저 트럭을 적재용량이 가장 큰 순서대로 정렬을 한 후,
    트럭을 순회하면서 적재할 컨테이너를 찾는다.
    컨테이너 무게를 가장 무거운 순서대로 정렬을 하면서 는다.
    """

    N, M = map(int, input().split())  # N = 컨테이너 수, M = 트럭 수
    weights = list(map(int, input().split()))
    used = [False] * N
    trucks = list(map(int, input().split()))
    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    # print(weights)
    # print(trucks)

    best = 0
    for t in trucks:
        for w in range(N):
            if used[w]:
                continue

            if weights[w] <= t:
                used[w] = True
                best += weights[w]
                break

    print(f"#{test_case} {best}")
