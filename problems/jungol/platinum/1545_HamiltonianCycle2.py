# JUNGOL 1545 해밀턴 순환회로 2
# 난이도: platinum5
# 분류: bitmask, dp, graph, tsp
# 핵심:
#   N이 최대 19이므로 DFS 백트래킹 O(N!)으로는 시간 초과가 난다.
#   방문한 정점 집합을 bitmask로 표현하고,
#   dp[mask][current] = mask 상태에서 current에 있을 때의 최소 비용으로 푼다.
# 시간 복잡도: O(N^2 * 2^N)
# 공간 복잡도: O(N * 2^N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 장소의 수, 1 <= N <= 19
#   cost: N x N 이동 비용 행렬
# - 출력:
#   1번 장소에서 출발해 모든 장소를 한 번씩 방문하고
#   다시 1번 장소로 돌아오는 최소 비용
# - 조건:
#   cost[i][j] == 0이면 i에서 j로 이동할 수 없다.
#   이동 비용은 단방향이다.
#   문제의 1번 장소는 코드에서 0번 인덱스로 사용한다.


# 2. 아이디어
# - 1681처럼 DFS로 모든 방문 순서를 보면 최악 O(N!)이라 N=19에서 불가능하다.
# - 방문한 장소 목록을 bitmask로 저장한다.
# - 예: N=5에서 00101은 0번, 2번 장소를 방문했다는 뜻이다.
# - dp[mask][current]는 mask에 포함된 장소들을 방문했고,
#   현재 current 장소에 있을 때의 최소 비용이다.
# - 아직 방문하지 않은 next_node로 이동하면서 다음 상태를 갱신한다.


# 3. 풀이 계획
# 1) 시작 상태 dp[1][0] = 0을 만든다.
# 2) mask를 0부터 전체 상태까지 순회한다.
# 3) 현재 mask에 포함된 current에서 아직 방문하지 않은 next_node로 이동한다.
# 4) next_mask = mask | (1 << next_node)를 갱신한다.
# 5) 모든 장소를 방문한 full 상태에서 다시 0번으로 돌아오는 비용을 더해 답을 구한다.


def solution(N, cost):
    if N == 1:
        return 0

    INF = 10**18
    full = (1 << N) - 1

    # dp[mask][current]
    # mask에 포함된 장소들을 방문했고,
    # 현재 current 장소에 있을 때의 최소 비용
    dp = [[INF] * N for _ in range(1 << N)]

    # 000...001 상태는 0번 장소, 즉 회사만 방문한 상태이다.
    dp[1][0] = 0

    for mask in range(1 << N):
        # 회사인 0번 장소가 포함되지 않은 상태는 만들 수 없는 상태이다.
        if (mask & 1) == 0:
            continue

        for current in range(N):
            if dp[mask][current] == INF:
                continue

            for next_node in range(N):
                # next_node 비트가 이미 켜져 있으면 이미 방문한 장소이다.
                if mask & (1 << next_node):
                    continue

                # 비용이 0이면 current에서 next_node로 갈 수 없다.
                if cost[current][next_node] == 0:
                    continue

                # next_node를 방문 목록에 추가한다.
                next_mask = mask | (1 << next_node)
                next_cost = dp[mask][current] + cost[current][next_node]

                # 같은 상태에 더 싼 비용으로 도착할 수 있으면 갱신한다.
                if next_cost < dp[next_mask][next_node]:
                    dp[next_mask][next_node] = next_cost

    answer = INF

    # 모든 장소를 방문한 뒤, 마지막 장소 current에서 회사 0번으로 돌아온다.
    for current in range(1, N):
        if cost[current][0] == 0:
            continue

        answer = min(answer, dp[full][current] + cost[current][0])

    return answer


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, cost))
