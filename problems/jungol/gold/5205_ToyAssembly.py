# JUNGOL 5205 장난감조립
# 난이도: gold
# 분류: graph, topological_sort, dp
# 핵심:
#   부품 조립 관계를 방향 그래프로 보고, 위상정렬 순서대로
#   각 부품을 만들기 위해 필요한 기본 부품 개수를 전파한다.
# 시간 복잡도: O(NM)
# 공간 복잡도: O(N^2 + M)

from collections import deque
import sys


# 1. 문제 이해
# - 완제품 N을 만들기 위해 필요한 기본 부품의 번호와 개수를 구한다.
# - 관계 (X, Y, K)는 X를 만들 때 Y가 K개 필요하다는 뜻이다.
# - 중간 부품은 출력하지 않고, 기본 부품만 번호순으로 출력한다.


# 2. 아이디어
# - Y가 있어야 X를 만들 수 있으므로 그래프를 Y -> X 방향으로 만든다.
# - indegree[X]는 X를 만들기 위해 먼저 처리되어야 하는 하위 부품 종류 수이다.
# - indegree가 0인 부품은 더 작은 부품으로 조립되지 않는 기본 부품이다.
# - need[part][basic]은 part 1개를 만들기 위해 basic 기본 부품이 몇 개 필요한지 저장한다.
# - 기본 부품 basic은 자기 자신 1개가 필요하므로 need[basic][basic] = 1이다.


# 3. 풀이 계획
# 1) 관계 (X, Y, K)를 읽어서 Y -> X 간선으로 저장한다.
# 2) indegree가 0인 기본 부품을 큐에 넣고 need[i][i] = 1로 초기화한다.
# 3) 큐에서 부품 current를 꺼낸다.
# 4) current가 필요한 상위 부품 next_part에 기본 부품 개수를 전달한다.
# 5) next_part의 indegree가 0이 되면 큐에 넣는다.
# 6) 마지막에 need[N]에서 값이 0보다 큰 기본 부품만 출력한다.


def solution(N, relations):
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for parent, child, count in relations:
        graph[child].append((parent, count))
        indegree[parent] += 1

    need = [[0] * (N + 1) for _ in range(N + 1)]
    queue = deque()
    basic_parts = []

    for part in range(1, N + 1):
        if indegree[part] == 0:
            queue.append(part)
            basic_parts.append(part)
            need[part][part] = 1

    while queue:
        current = queue.popleft()

        for next_part, count in graph[current]:
            for basic in basic_parts:
                need[next_part][basic] += need[current][basic] * count

            indegree[next_part] -= 1

            if indegree[next_part] == 0:
                queue.append(next_part)

    answer = []

    for basic in basic_parts:
        if need[N][basic] > 0:
            answer.append((basic, need[N][basic]))

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    relations = [tuple(map(int, input().split())) for _ in range(M)]

    for part, count in solution(N, relations):
        print(part, count)
