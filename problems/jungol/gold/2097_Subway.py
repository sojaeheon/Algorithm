# JUNGOL 2097 지하철
# 난이도: gold
# 분류: graph, dijkstra, shortest_path, path_reconstruction
# 핵심:
#   1번 역에서 목적 역까지의 최소 비용을 구하고 이전 역을 역추적한다.
# 시간 복잡도: O(N^2 log N)
# 공간 복잡도: O(N^2)

import sys


# 1. 문제 이해
# - 입력: 역의 수 N, 목적 역 M, N×N 이동 비용 행렬
# - 출발 역은 1번이다.
# - 출력: 최소 비용과 최소 비용으로 이동하는 경로


# 2. 아이디어
# - 비용 행렬을 인접 그래프로 보고 1번 역에서 다익스트라를 실행한다.
# - 거리가 갱신될 때 previous[next_station]에 현재 역을 저장한다.
# - 목적 역부터 previous를 따라간 뒤 뒤집으면 최단 경로가 된다.


def solution(N, destination, costs):
    # TODO: 다익스트라로 최소 비용과 경로를 구한다.
    # return minimum_cost, path
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, destination = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(N)]

    minimum_cost, path = solution(N, destination, costs)
    print(minimum_cost)
    print(*path)
