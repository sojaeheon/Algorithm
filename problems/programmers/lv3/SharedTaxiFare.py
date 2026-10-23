# Programmers 72413 합승 택시 요금
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72413
# 난이도: LV3

import heapq


def dijkstra(start, graph):
    INF = float("inf")
    n = len(graph) - 1

    distance = [INF] * (n + 1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        current_cost, current_nd = heapq.heappop(hq)

        if current_cost > distance[current_nd]:
            continue

        for next_nd, cost in graph[current_nd]:
            next_cost = current_cost + cost

            if distance[next_nd] <= next_cost:
                continue

            distance[next_nd] = next_cost
            heapq.heappush(hq, (next_cost, next_nd))

    return distance


def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n + 1)]

    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    start_distance = dijkstra(s, graph)
    a_distance = dijkstra(a, graph)
    b_distance = dijkstra(b, graph)

    answer = min(
        start_distance[i] + a_distance[i] + b_distance[i]
        for i in range(1, n + 1)
    )

    return answer
