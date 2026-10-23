# Programmers 42861 섬 연결하기
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 난이도: LV3
# 풀이: Prim
import heapq

def solution(n, costs):
    answer = 0

    graph = [[] for _ in range(n)]

    for a,b,cost in costs:
        graph[a].append((cost,b))
        graph[b].append((cost,a))

    visited = [False] * (n)
    pq = [(0,0)]

    count = 0

    while pq:
        cost, now = heapq.heappop(pq)

        if visited[now]:
            continue

        visited[now]=True
        answer+=cost
        count += 1

        for nxt_cost,nxt in graph[now]:
            if not visited[nxt]:
                heapq.heappush(pq,(nxt_cost,nxt))

    if count != n:
        return -1

    return answer
