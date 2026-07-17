# JUNGOL 1681 해밀턴 순환회로
# 난이도: silver1
# 분류: dfs, backtracking, graph, tsp
# 핵심:
#   1번 정점에서 출발해 모든 정점을 정확히 한 번씩 방문한 뒤
#   다시 1번 정점으로 돌아오는 최소 비용을 찾는다.
#   비용이 0인 간선은 이동할 수 없는 간선이다.
# 시간 복잡도: O(N!)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 정점의 수
#   cost: N x N 비용 행렬
# - 출력:
#   1번 정점에서 출발해 모든 정점을 한 번씩 방문하고,
#   다시 1번 정점으로 돌아오는 최소 비용
# - 조건:
#   cost[i][j] == 0이면 i에서 j로 이동할 수 없다.
#   문제의 1번 정점은 코드에서 0번 인덱스로 사용한다.


# 2. 아이디어
# - 해밀턴 순환회로는 "모든 정점 1번씩 방문 + 시작점으로 복귀"이다.
# - 시작점은 0번 정점으로 고정한다.
# - DFS 백트래킹으로 가능한 방문 순서를 만든다.
# - 이미 방문한 정점은 다시 방문하지 않는다.
# - 현재 비용이 이미 정답 이상이면 더 탐색하지 않고 가지치기한다.
# - 모든 정점을 방문했을 때 시작점으로 돌아갈 수 있으면 정답을 갱신한다.


# 3. 풀이 계획
# 1) 시작점 0을 방문 처리한다.
# 2) dfs(current, count, total_cost)로 탐색한다.
# 3) 다음 정점은 아직 방문하지 않았고, 비용이 0이 아닌 곳만 선택한다.
# 4) count == N이면 모든 정점을 방문한 상태이다.
# 5) 이때 current에서 시작점 0으로 돌아갈 수 있으면 최소 비용을 갱신한다.


def solution(N, cost):
    INF = 10**18
    answer = INF

    visited = [False] * N
    visited[0] = True

    def dfs(current, count, total_cost):
        nonlocal answer

        # 현재까지 비용이 이미 최소 후보 이상이면 더 볼 필요가 없다.
        if total_cost >= answer:
            return

        # 모든 정점을 방문했다면 시작점으로 돌아갈 수 있는지 확인한다.
        if count == N:
            if cost[current][0] != 0:
                answer = min(answer, total_cost + cost[current][0])
            return

        for next_node in range(N):
            if visited[next_node]:
                continue

            if cost[current][next_node] == 0:
                continue

            visited[next_node] = True
            dfs(
                next_node,
                count + 1,
                total_cost + cost[current][next_node],
            )
            visited[next_node] = False

    dfs(0, 1, 0)

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, cost))
