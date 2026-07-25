# JUNGOL 3118 최단경로2
# 난이도: gold
# 분류: graph, dijkstra, shortest_path
# 핵심:
#   음수가 아닌 가중치를 가진 방향 그래프에서 1번부터 N번까지의 최단 거리를 구한다.
# 시간 복잡도: O((N + M) log N)
# 공간 복잡도: O(N + M)

import sys


# 1. 문제 이해
# - 입력: 정점 수 N, 간선 수 M, M개의 (시작점, 끝점, 비용)
# - 출력: 1번 정점에서 N번 정점까지의 최단 거리


# 2. 아이디어
# - 인접 리스트로 방향 그래프를 만든다.
# - 최소 힙에 (현재 거리, 정점)을 저장한다.
# - 꺼낸 거리가 이미 저장된 거리보다 크면 오래된 항목이므로 건너뛴다.
# - N번 정점을 확정하면 조기 종료할 수 있다.


def solution(N, M, edges):
    # TODO: 우선순위 큐 다익스트라로 1번에서 N번까지의 최단 거리를 구한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, M, edges))
