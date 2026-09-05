# JUNGOL 2109 꿀꿀이 축제
# 난이도: gold
# 분류: graph, dijkstra, shortest_path
# 핵심:
#   X에서 각 마을로 가는 거리와 각 마을에서 X로 오는 거리를 각각 구한다.
#   간선을 뒤집으면 모든 마을에서 X로 오는 거리를 다익스트라 한 번으로 계산할 수 있다.
# 시간 복잡도: O((N + M) log N)
# 공간 복잡도: O(N + M)

import sys
import heapq


# 1. 문제 이해
# - N개 마을, M개 단방향 도로, 축제 마을 X가 주어진다.
# - 각 마을에서 X까지 갔다가 다시 돌아오는 최단 왕복 시간을 구한다.
# - 출력: 모든 꿀꿀이 중 가장 긴 최단 왕복 시간


# 2. 아이디어
# - 원본 그래프에서 X를 시작점으로 다익스트라: X -> 각 마을
# - 역방향 그래프에서 X를 시작점으로 다익스트라: 각 마을 -> X
# - 두 거리의 합 중 최댓값이 정답이다.


def solution(N, M, X, roads):
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for start, end, time in roads:
        graph[start].append((end, time))
        reverse_graph[end].append((start, time))

    def dijkstra(start, edges):
        distances = [float("inf")] * (N + 1)
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            distance, node = heapq.heappop(queue)
            if distance != distances[node]:
                continue

            for next_node, cost in edges[node]:
                next_distance = distance + cost
                if next_distance < distances[next_node]:
                    distances[next_node] = next_distance
                    heapq.heappush(queue, (next_distance, next_node))

        return distances

    distances_from_x = dijkstra(X, graph)
    distances_to_x = dijkstra(X, reverse_graph)

    return max(
        distances_from_x[village] + distances_to_x[village]
        for village in range(1, N + 1)
    )


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, X = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, M, X, roads))
