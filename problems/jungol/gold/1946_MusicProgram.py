# JUNGOL 1946 음악프로그램
# 난이도: gold
# 분류: graph, topological_sort, queue
# 핵심:
#   각 PD가 정한 가수 순서를 방향 간선으로 바꾸고 위상정렬한다.
#   모든 가수를 정렬하지 못하면 순서에 모순이 있는 것이다.
# 시간 복잡도: O(N + E)
# 공간 복잡도: O(N + E)

from collections import deque
import sys


# 1. 문제 이해
# - N명의 가수와 M명의 PD가 정한 부분 순서가 주어진다.
# - 각 줄은 가수 수 K와 K명의 순서를 나타낸다.
# - 가능한 전체 순서를 한 줄에 한 명씩 출력하고, 불가능하면 0을 출력한다.


# 2. 아이디어
# - 한 순서가 a, b, c라면 a -> b, b -> c 간선을 추가한다.
# - 진입 차수가 0인 가수부터 큐에 넣어 위상정렬한다.
# - 결과 길이가 N보다 작으면 사이클이 있으므로 0을 반환한다.


def solution(N, orders):
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    # PD가 정한 순서에서 서로 이웃한 가수 사이에 방향 간선을 만든다.
    # 예: [1, 4, 3]이면 1 -> 4, 4 -> 3
    for order in orders:
        for index in range(len(order) - 1):
            before = order[index]
            after = order[index + 1]

            graph[before].append(after)
            indegree[after] += 1

    queue = deque()

    # 앞에 와야 하는 가수가 없는 가수부터 시작한다.
    for singer in range(1, N + 1):
        if indegree[singer] == 0:
            queue.append(singer)

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for next_singer in graph[current]:
            indegree[next_singer] -= 1

            if indegree[next_singer] == 0:
                queue.append(next_singer)

    # 모든 가수를 정렬하지 못했다면 순서 조건에 사이클이 있는 것이다.
    if len(result) != N:
        return []

    return result


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    orders = [list(map(int, input().split()))[1:] for _ in range(M)]

    answer = solution(N, orders)

    if answer:
        print(*answer, sep="\n")
    else:
        print(0)
