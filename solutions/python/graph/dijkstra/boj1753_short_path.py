"""
방향그래프가 주어지면, 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구해야 한다.
        단, 모든 간선의 가중치는 10이하의 자연수이다. (모든 간선의 가중치가 다르다.)

=> 다익스트라
"""

import heapq
import sys

input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    K = int(input())

    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))

    INF = float("INF")
    dist = [INF] * (V + 1)
    dist[K] = 0

    heap = []
    heapq.heappush(heap, (0, K))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > dist[cur_node]:
            continue

        for nxt_node, weight in graph[cur_node]:
            new_dist = cur_dist + weight

            if new_dist < dist[nxt_node]:
                dist[nxt_node] = new_dist
                heapq.heappush(heap, (new_dist, nxt_node))

    for i in range(1, V + 1):
        if dist[i] == INF:
            print("INF")
            continue

        print(dist[i])


main()

"""
5 6
1
5 1 1
1 2 6
1 3 3
2 3 4
2 4 5
3 4 6
"""
