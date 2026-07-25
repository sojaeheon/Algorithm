# JUNGOL 1060 최소비용신장트리
# 난이도: gold
# 분류: graph, mst, prim
# 핵심:
#   비용 행렬에서 아직 연결되지 않은 학원 중 연결 비용이 가장 작은 곳을 선택한다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력: 학원 수 N (3 <= N <= 100), N×N 연결 비용 행렬
# - 모든 학원을 연결하되 전체 연결 비용을 최소화한다.
# - 출력: 최소 신장 트리의 비용


# 2. 아이디어
# - 완전 그래프가 비용 행렬로 주어지고 N이 작으므로 배열 기반 Prim이 간단하다.
# - min_cost[v]는 현재 트리에서 v를 연결하는 최소 간선 비용이다.
# - 매 단계 방문하지 않은 정점 중 min_cost가 가장 작은 정점을 선택한다.


def solution(N, costs):
    # TODO: Prim 알고리즘으로 최소 신장 트리 비용을 계산한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, costs))
