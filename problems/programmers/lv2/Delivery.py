# Programmers 배달
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 난이도: LV2
# 분류: graph, dijkstra, shortest_path
# 핵심:
#   1번 마을에서 각 마을까지의 최단시간을 구하고,
#   최단시간이 K 이하인 마을의 개수를 센다.
# 시간 복잡도: O((N + E) log N)
# 공간 복잡도: O(N + E)


# 1. 문제 이해
# - 입력:
#   N: 마을의 개수
#   road: [마을 a, 마을 b, 이동 시간 c] 형태의 양방향 도로 목록
#   K: 배달 가능한 최대 시간
# - 출력:
#   1번 마을에서 K 시간 이하로 갈 수 있는 마을의 개수
# - 조건:
#   같은 두 마을을 연결하는 도로가 여러 개 있을 수 있다.
#   1번 마을 자체도 배달 가능한 마을에 포함한다.


# 2. 아이디어
# - 모든 도로의 이동 시간이 양수이므로 다익스트라 알고리즘을 사용한다.
# - 양방향 도로이므로 a -> b와 b -> a를 모두 인접 리스트에 저장한다.
# - 1번 마을부터 각 마을까지의 최단시간을 구한다.
# - 최단시간이 K 이하인 마을만 센다.


# 3. 풀이 계획
# 1) road를 이용해 양방향 인접 리스트를 만든다.
# 2) 1번 마을의 거리는 0, 나머지는 무한대로 초기화한다.
# 3) 최소 힙으로 아직 확인할 마을과 현재 최단시간을 관리한다.
# 4) 더 짧은 경로를 찾으면 거리를 갱신하고 힙에 넣는다.
# 5) 최종 거리가 K 이하인 마을의 개수를 반환한다.

import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    distance = [float("inf")] * (N + 1)
    distance[1] = 0
    pq = [(0, 1)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # 최소 힙이므로 현재 비용이 K를 넘으면 이후 경로도 모두 K를 넘는다.
        if current_cost > K:
            break

        if distance[current_node] < current_cost:
            continue

        for next_node, road_cost in graph[current_node]:
            new_cost = current_cost + road_cost

            if new_cost <= K and new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return sum(distance[village] <= K for village in range(1, N + 1))



if __name__ == "__main__":
    print(
        solution(
            5,
            [
                [1, 2, 1],
                [2, 3, 3],
                [5, 2, 2],
                [1, 4, 2],
                [5, 3, 1],
                [5, 4, 2],
            ],
            3,
        )
    )  # 예상: 4

    print(
        solution(
            6,
            [
                [1, 2, 1],
                [1, 3, 2],
                [2, 3, 2],
                [3, 4, 3],
                [3, 5, 2],
                [3, 5, 3],
                [5, 6, 1],
            ],
            4,
        )
    )  # 예상: 4
