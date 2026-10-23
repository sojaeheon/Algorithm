# JUNGOL 1440 가장 가까운 공통 조상 찾기
# https://jungol.co.kr/problem/1440
# 분류: tree, lowest_common_ancestor
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

import sys
from collections import deque


def solution(N, edges, node_a, node_b):
    parent = [0] * (N + 1)
    children = [[] for _ in range(N + 1)]
    has_parent = [False] * (N + 1)

    # 입력으로 주어진 부모-자식 관계를 그대로 저장한다.
    for parent_node, child_node in edges:
        parent[child_node] = parent_node
        children[parent_node].append(child_node)
        has_parent[child_node] = True

    # 부모가 없는 노드가 이 트리의 루트이다.
    root = next(
        node for node in range(1, N + 1) if not has_parent[node]
    )

    # 루트부터 BFS를 수행해 각 노드의 깊이를 계산한다.
    depth = [0] * (N + 1)
    queue = deque([root])

    while queue:
        current = queue.popleft()

        for child in children[current]:
            depth[child] = depth[current] + 1
            queue.append(child)

    # 두 노드의 깊이를 같게 만든다.
    while depth[node_a] > depth[node_b]:
        node_a = parent[node_a]

    while depth[node_b] > depth[node_a]:
        node_b = parent[node_b]

    # 같은 노드에서 만날 때까지 동시에 부모로 이동한다.
    while node_a != node_b:
        node_a = parent[node_a]
        node_b = parent[node_b]

    return node_a

if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    node_a, node_b = map(int, input().split())

    print(solution(N, edges, node_a, node_b))
