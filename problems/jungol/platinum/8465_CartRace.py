# JUNGOL 8465 리어카 경주
# 문제: https://jungol.co.kr/problem/8465
# 난이도: Platinum 4
# 분류: graph, reachability, topological_sort, dp
# 시간 복잡도: O(N + M)
# 공간 복잡도: O(N + M)

import sys
from collections import deque


MOD = 1_000_000_000


def reachable_from(start, graph):
    visited = [False] * len(graph)
    visited[start] = True
    queue = [start]

    for node in queue:
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return visited


def solution(N, roads):
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for start, end in roads:
        graph[start].append(end)
        reverse_graph[end].append(start)

    # 1번에서 도달할 수 있고 최종적으로 2번에 갈 수 있는 마을만 남긴다.
    from_start = reachable_from(1, graph)
    to_finish = reachable_from(2, reverse_graph)
    relevant = [
        from_start[node] and to_finish[node]
        for node in range(N + 1)
    ]

    indegree = [0] * (N + 1)
    relevant_count = 0

    for node in range(1, N + 1):
        if not relevant[node]:
            continue
        relevant_count += 1
        for next_node in graph[node]:
            if relevant[next_node]:
                indegree[next_node] += 1

    queue = deque(
        node
        for node in range(1, N + 1)
        if relevant[node] and indegree[node] == 0
    )
    path_count = [0] * (N + 1)
    path_count[1] = 1
    processed_count = 0

    while queue:
        node = queue.popleft()
        processed_count += 1

        for next_node in graph[node]:
            if not relevant[next_node]:
                continue

            # 평행 도로도 각각 다른 경로로 센다.
            path_count[next_node] = (
                path_count[next_node] + path_count[node]
            ) % MOD
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    if processed_count != relevant_count:
        return "inf"

    return path_count[2]


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, roads))
