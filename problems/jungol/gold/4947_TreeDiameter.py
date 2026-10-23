# JUNGOL 4947 Tree Diameter
# https://jungol.co.kr/problem/4947

from collections import deque
import sys


def solution(N, edges):
    graph = [[] for _ in range(N + 1)]

    # 부모와 자식으로 주어지지만, 두 정점 사이의 거리를 구해야 하므로
    # 양쪽으로 이동할 수 있는 무방향 그래프로 저장한다.
    for parent, child in edges:
        graph[parent].append(child)
        graph[child].append(parent)

    def find_farthest(start):
        distance = [-1] * (N + 1)
        distance[start] = 0

        queue = deque([start])
        farthest_node = start

        while queue:
            current = queue.popleft()

            for next_node in graph[current]:
                if distance[next_node] != -1:
                    continue

                distance[next_node] = distance[current] + 1
                queue.append(next_node)

                if distance[next_node] > distance[farthest_node]:
                    farthest_node = next_node

        return farthest_node, distance[farthest_node]

    # 임의의 정점에서 가장 먼 정점은 지름을 이루는 한쪽 끝점이다.
    diameter_start, _ = find_farthest(1)

    # 그 끝점에서 가장 먼 정점까지의 거리가 트리의 지름이다.
    _, diameter = find_farthest(diameter_start)

    return diameter


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

    print(solution(N, edges))
