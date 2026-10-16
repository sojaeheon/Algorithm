# Programmers 118669 등산코스 정하기
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 난이도: LV3
# 분류: graph, dijkstra, multi_source, minimax_path
# 핵심:
#   모든 출입구를 시작점으로 넣는 Multi-source Dijkstra를 사용한다.
#   경로 비용의 합이 아니라 경로에서 가장 큰 간선 비용인 intensity를 최소화한다.
# 시간 복잡도: O((N + E) log N)
# 공간 복잡도: O(N + E)

import heapq


# 1. 문제 이해
# - 입력:
#   n: 지점의 개수
#   paths: [지점1, 지점2, 이동 시간] 형태의 양방향 등산로 목록
#   gates: 출입구 번호 목록
#   summits: 산봉우리 번호 목록
# - 출력:
#   [선택한 산봉우리 번호, 최소 intensity]
# - intensity:
#   한 등산코스에서 지나간 등산로 이동 시간 중 가장 큰 값
# - 우선순위:
#   intensity가 가장 작은 코스를 선택한다.
#   intensity가 같으면 산봉우리 번호가 작은 것을 선택한다.


# 2. 아이디어
# - 모든 출입구 중 어디에서 출발해도 되므로 출입구를 모두 힙에 넣고 시작한다.
# - intensity[node]는 어떤 출입구에서 node까지 갈 때 가능한 최소 intensity이다.
# - 현재 지점까지의 intensity가 current_intensity이고 다음 등산로가 weight라면,
#   다음 지점까지의 intensity는 두 값 중 큰 값이다.
#
#   next_intensity = max(current_intensity, weight)
#
# - 더 작은 next_intensity를 찾았을 때만 갱신한다.
# - 산봉우리에 도착하면 답 후보가 되지만 산봉우리 너머로는 이동하지 않는다.
# - 다른 출입구를 중간에 지나가는 코스도 허용되지 않도록 그래프 또는 탐색에서 막는다.


# 3. 풀이 계획
# 1) paths로 양방향 인접 리스트를 만든다.
# 2) 출입구와 산봉우리를 빠르게 확인할 수 있도록 set을 만든다.
# 3) 모든 출입구의 intensity를 0으로 두고 힙에 함께 넣는다.
# 4) 힙에서 intensity가 가장 작은 지점을 꺼낸다.
# 5) 산봉우리라면 더 이동하지 않는다.
# 6) 이웃으로 갈 때 max(현재 intensity, 등산로 시간)을 계산한다.
# 7) 기존 intensity보다 작으면 갱신하고 힙에 넣는다.
# 8) 산봉우리를 번호순으로 확인해 intensity가 가장 작은 답을 반환한다.


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    for start, end, weight in paths:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    gate_set = set(gates)
    summit_set = set(summits)

    INF = float("inf")
    intensity = [INF] * (n + 1)
    heap = []

    # 어느 출입구에서 시작하든 처음 intensity는 0이다.
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(heap, (0, gate))

    while heap:
        current_intensity, current_node = heapq.heappop(heap)

        # 이미 더 낮은 intensity로 갱신된 오래된 항목은 무시한다.
        if current_intensity != intensity[current_node]:
            continue

        # 산봉우리는 코스의 끝이므로 산봉우리 너머로 이동하지 않는다.
        if current_node in summit_set:
            continue

        for next_node, weight in graph[current_node]:
            # 출발 이후 다른 출입구를 통과할 수 없다.
            if next_node in gate_set:
                continue

            next_intensity = max(current_intensity, weight)

            if next_intensity < intensity[next_node]:
                intensity[next_node] = next_intensity
                heapq.heappush(heap, (next_intensity, next_node))

    # (intensity, 산봉우리 번호) 순서로 비교하면 동점일 때 작은 번호가 선택된다.
    answer_summit = min(
        summits,
        key=lambda summit: (intensity[summit], summit),
    )

    return [answer_summit, intensity[answer_summit]]


if __name__ == "__main__":
    print(
        solution(
            6,
            [
                [1, 2, 3],
                [2, 3, 5],
                [2, 4, 2],
                [2, 5, 4],
                [3, 4, 4],
                [4, 5, 3],
                [4, 6, 1],
                [5, 6, 1],
            ],
            [1, 3],
            [5],
        )
    )  # 예상: [5, 3]

    print(
        solution(
            7,
            [
                [1, 4, 4],
                [1, 6, 1],
                [1, 7, 3],
                [2, 5, 2],
                [3, 7, 4],
                [5, 6, 6],
            ],
            [1],
            [2, 3, 4],
        )
    )  # 예상: [3, 4]

    print(
        solution(
            7,
            [
                [1, 2, 5],
                [1, 4, 1],
                [2, 3, 1],
                [2, 6, 7],
                [4, 5, 1],
                [5, 6, 1],
                [6, 7, 1],
            ],
            [3, 7],
            [1, 5],
        )
    )  # 예상: [5, 1]

    print(
        solution(
            5,
            [
                [1, 3, 10],
                [1, 4, 20],
                [2, 3, 4],
                [2, 4, 6],
                [3, 5, 20],
                [4, 5, 6],
            ],
            [1, 2],
            [5],
        )
    )  # 예상: [5, 6]
