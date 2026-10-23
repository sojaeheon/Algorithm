# JUNGOL 1946 Music Program
# https://jungol.co.kr/problem/1946

import sys
from collections import deque


def solution(N, orders):
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    # 한 PD가 정한 순서에서 연속된 두 가수를 방향 간선으로 연결한다.
    # 예: [1, 4, 3]은 1 -> 4, 4 -> 3이 된다.
    for order in orders:
        for index in range(len(order) - 1):
            before = order[index]
            after = order[index + 1]

            graph[before].append(after)
            indegree[after] += 1

    queue = deque()

    # 자신보다 먼저 나와야 하는 가수가 없는 가수부터 시작한다.
    for singer in range(1, N + 1):
        if indegree[singer] == 0:
            queue.append(singer)

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        # 현재 가수를 배치했으므로 다음 가수들의 진입 차수를 줄인다.
        for next_singer in graph[current]:
            indegree[next_singer] -= 1

            if indegree[next_singer] == 0:
                queue.append(next_singer)

    # 모든 가수를 배치하지 못했다면 순서 조건에 순환이 존재한다.
    if len(result) != N:
        return []

    return result


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    orders = []

    for _ in range(M):
        order = list(map(int, input().split()))
        orders.append(order[1:])

    answer = solution(N, orders)

    if answer:
        print(*answer, sep="\n")
    else:
        print(0)
