# Programmers 49189 가장 먼 노드
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 난이도: LV3

from collections import deque

def solution(n, edge):
    graph  = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 거리배열 만들기
    distance = [-1] * (n+1)
    distance[1] = 0

    que = deque([1])

    while que:
        current = que.popleft()

        for next_node in graph[current]:
            if distance[next_node]  != -1:
                continue
            distance[next_node] = distance[current] + 1
            que.append(next_node)

    max_distance  = max(distance[1:])
    answer = distance[1:].count(max_distance)


    return answer
