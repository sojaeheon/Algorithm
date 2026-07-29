# JUNGOL 3865 Ski Course Rating
# 문제: https://jungol.co.kr/problem/3865
# 난이도: gold
# 분류: graph, kruskal, union_find, offline_query
# 핵심:
#   높이 차가 작은 인접 간선부터 처리하면서 컴포넌트를 합친다.
#   컴포넌트 크기가 처음 T 이상이 되는 간선 가중치가 그 안의 시작점에 대한 난이도이다.
# 시간 복잡도: O(MN log(MN))
# 공간 복잡도: O(MN)

import sys


# 1. 문제 이해
# - M×N 격자 각 칸의 고도가 주어진다.
# - 상하좌우로 이동하며, 한 번 이동할 때 허용되는 최대 높이 차를 D라고 한다.
# - 각 시작점에서 적어도 T개의 칸에 도달할 수 있게 하는 최소 D를 구한다.
# - 모든 시작점의 최소 D 합을 출력한다.


# 2. 입력
# - M, N, T
# - M줄: 각 칸의 고도
# - M줄: 시작점이면 1, 아니면 0


def solution(M, N, T, heights, starting_points):
    if T == 1:
        return 0

    cell_count = M * N
    edges = []

    # 같은 무방향 간선을 중복해서 만들지 않도록 오른쪽과 아래쪽만 확인한다.
    for row in range(M):
        for col in range(N):
            current = row * N + col

            if col + 1 < N:
                right = current + 1
                cost = abs(heights[row][col] - heights[row][col + 1])
                edges.append((cost, current, right))

            if row + 1 < M:
                down = current + N
                cost = abs(heights[row][col] - heights[row + 1][col])
                edges.append((cost, current, down))

    edges.sort()

    parent = list(range(cell_count))
    size = [1] * cell_count

    # 아직 난이도가 확정되지 않은 시작점의 수를 컴포넌트별로 관리한다.
    pending_starts = [
        starting_points[index // N][index % N]
        for index in range(cell_count)
    ]

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = 0

    for cost, first, second in edges:
        root_first = find(first)
        root_second = find(second)

        if root_first == root_second:
            continue

        if size[root_first] < size[root_second]:
            root_first, root_second = root_second, root_first

        parent[root_second] = root_first
        size[root_first] += size[root_second]
        pending_starts[root_first] += pending_starts[root_second]

        # 이 컴포넌트가 처음 T개 이상의 칸을 포함하게 된 순간이다.
        # 이미 처리된 시작점은 pending_starts에서 제거되어 중복 계산되지 않는다.
        if size[root_first] >= T and pending_starts[root_first] > 0:
            answer += cost * pending_starts[root_first]
            pending_starts[root_first] = 0

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    M, N, T = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(M)]
    starting_points = [list(map(int, input().split())) for _ in range(M)]

    print(solution(M, N, T, heights, starting_points))
