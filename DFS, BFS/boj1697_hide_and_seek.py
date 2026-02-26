from collections import deque

N, K = map(int, input().split())  # N = 수빈이가 있는 위치, K = 동생이 있는 위치 (0 <= N, K <= 100,000)
"""
수빈이는 두 가지의 행동을 할 수 있다.
    1) 걷는다.
            => 걷는 경우에는 1초 후에, X-1 또는 X+1로 이동하게 된다.
    2) 순간이동한다.
            => 순간이동의 경우에는 1초 후에, 2*X의 위치로 이동하게 된다.       
            
[내가 이전에 잘못했던 포인트들]

1) 그리디(순간이동 우선)로 줄이기 시도:
   - 'K를 넘지 않게 순간이동' 같은 규칙은 최적 보장 X (반례 존재)
   - 이 문제는 규칙으로 결정할 수 없고, 모든 상태를 최단거리 순으로 탐색해야 함(BFS)

2) 방문처리(visited/dist) 없이 큐에 계속 넣기:
   - 같은 위치가 무한히 다시 큐에 들어가서 폭발(시간초과)
   - 예: 5 -> 4 -> 5 -> 4 ... 같은 사이클이 계속 생김
   - 해결: dist[nx] == -1 (처음 방문일 때만 큐에 넣기)

3) deque에서 (nx, time) in q 같은 체크:
   - deque에서 in 연산은 O(큐 길이) 선형 탐색이라 매우 느림
   - BFS는 큐가 커지므로 이런 방식은 시간초과 유발
   - 해결: 큐 검색이 아니라 dist/visited 배열로 O(1) 체크

4) 범위 제한 안 해서 상태 공간 폭발:
   - 문제는 0~100000만 유효한데, 범위 체크 없으면 -1, 200000, 400000... 무한 확장
   - 해결: 0 <= nx <= MAX 체크 필수

5) start > target 처리 부호 실수:
   - start가 더 크면 순간이동이 의미 없고 -1만 하면 됨
   - 정답은 start - target (음수로 return하면 틀림)

6) 큐에 int가 아니라 [x] 같은 리스트로 넣는 실수:
   - q.append([start]) 하면 pop한 x가 list가 되어 x-1 같은 연산에서 터짐(TypeError)
   - 해결: q에는 정수 그대로 넣기 (q.append(start))  
"""


def find_sister(start, target):
    if start == target:
        return 0
    elif start > target:
        return start - target

    MAX = 100000
    dist = [-1] * (MAX + 1)
    dist[start] = 0

    q = deque()
    q.append(start)
    while q:
        x = q.popleft()

        if x == target:
            return dist[x]

        options = (x - 1, x + 1, x * 2)
        for nx in options:
            if 0 <= nx <= 100000 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                if nx == target:
                    return dist[nx]
                q.append(nx)


print(find_sister(N, K))
