# Programmers 72413 합승 택시 요금
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72413
# 풀이: Floyd-Warshall
# 시간 복잡도: O(N^3)
# 공간 복잡도: O(N^2)


def solution(n, s, a, b, fares):
    INF = float("inf")
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0이다.
    for node in range(1, n + 1):
        distance[node][node] = 0

    # 택시 요금은 양방향이다.
    for start, end, fare in fares:
        distance[start][end] = min(distance[start][end], fare)
        distance[end][start] = min(distance[end][start], fare)

    # middle을 경유했을 때 더 저렴하면 최단 거리를 갱신한다.
    for middle in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                distance[start][end] = min(
                    distance[start][end],
                    distance[start][middle] + distance[middle][end],
                )

    answer = INF

    # split까지 합승하고, split에서 A와 B의 목적지로 따로 이동한다.
    for split in range(1, n + 1):
        total_fare = (
            distance[s][split]
            + distance[split][a]
            + distance[split][b]
        )
        answer = min(answer, total_fare)

    return answer
