# JUNGOL 2574 사회망 서비스(SNS)
# 문제: https://jungol.co.kr/problem/2574
# 난이도: Gold 3
# 분류: tree, dynamic_programming
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

import sys
from array import array


def solution(N, edges):
    # N이 매우 크므로 Python 객체 기반 인접 리스트 대신 정수 배열로
    # 양방향 연결 리스트를 만들어 메모리 사용량을 줄인다.
    head = array("i", [-1]) * (N + 1)
    to = array("i")
    next_edge = array("i")

    for first, second in edges:
        to.append(second)
        next_edge.append(head[first])
        head[first] = len(to) - 1

        to.append(first)
        next_edge.append(head[second])
        head[second] = len(to) - 1

    # 1번을 루트로 정하고 부모와 탐색 순서를 만든다.
    parent = array("i", [0]) * (N + 1)
    parent[1] = -1
    order = array("i")
    stack = array("i", [1])

    while stack:
        node = stack.pop()
        order.append(node)

        edge_index = head[node]

        while edge_index != -1:
            next_node = to[edge_index]

            if next_node != parent[node]:
                parent[next_node] = node
                stack.append(next_node)

            edge_index = next_edge[edge_index]

    # early[node]: node가 얼리어답터일 때 서브트리의 최소 인원
    # normal[node]: node가 얼리어답터가 아닐 때 서브트리의 최소 인원
    early = array("i", [1]) * (N + 1)
    normal = array("i", [0]) * (N + 1)

    # 자식부터 계산하기 위해 탐색 순서를 거꾸로 확인한다.
    for node in reversed(order):
        edge_index = head[node]

        while edge_index != -1:
            child = to[edge_index]

            if parent[child] == node:
                normal[node] += early[child]
                early[node] += min(early[child], normal[child])

            edge_index = next_edge[edge_index]

    return min(early[1], normal[1])


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    edges = (
        tuple(map(int, input().split()))
        for _ in range(N - 1)
    )

    print(solution(N, edges))
