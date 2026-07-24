# JUNGOL 1912 미로 탐색
# 난이도: gold4
# 분류: graph, dfs, stack, sorting
# 핵심:
#   1번 방에서 시작한다.
#   현재 방과 연결된 방 중 아직 방문하지 않은 방이 있으면,
#   그중 번호가 가장 작은 방으로 이동한다.
#   더 갈 수 있는 방이 없으면 왔던 길로 되돌아간다.
#   방을 처음 방문한 순서를 출력한다.
# 시간 복잡도: O(M log M + N + M)
# 공간 복잡도: O(N + M)

import sys


# 1. 문제 이해
# - 입력:
#   N: 방의 수, 2 <= N <= 100000
#   M: 문의 수, 1 <= M <= 500000
#   edges: 서로 연결된 두 방 번호
# - 출력:
#   동현이가 처음 방문한 순서대로 N개의 방 번호를 한 줄에 출력한다.
# - 조건:
#   모든 방은 서로 연결되어 있다.
#   현재 방에서 방문하지 않은 인접 방이 여러 개라면 번호가 가장 작은 방으로 이동한다.


# 2. 아이디어
# - 방과 문은 그래프로 볼 수 있다.
# - 문은 양방향이므로 a와 b가 연결되어 있으면 a -> b, b -> a를 모두 저장한다.
# - 번호가 작은 방부터 가야 하므로 각 방의 인접 리스트를 오름차순 정렬한다.
# - DFS처럼 깊게 들어가고, 더 갈 곳이 없으면 stack으로 되돌아간다.
# - N이 최대 100000이므로 재귀 DFS 대신 반복문 DFS를 사용한다.
# - 각 방마다 다음에 확인할 인접 방 위치를 next_index에 저장한다.


# 3. 풀이 계획
# 1) 양방향 그래프를 인접 리스트로 만든다.
# 2) 각 방의 인접 리스트를 오름차순 정렬한다.
# 3) 1번 방을 방문 처리하고 stack에 넣는다.
# 4) stack의 맨 위를 현재 방으로 보고, 아직 방문하지 않은 가장 작은 인접 방을 찾는다.
# 5) 찾으면 방문 처리하고 정답에 추가한 뒤 stack에 넣는다.
# 6) 더 갈 방이 없으면 stack에서 pop해서 이전 방으로 되돌아간다.


def solution(N, M, edges):
    # 방 번호가 1부터 N까지이므로 N + 1칸을 만든다.
    # graph[room]에는 room과 연결된 방 번호들이 들어간다.
    graph = [[] for _ in range(N + 1)]

    # 문은 양방향이므로 양쪽 인접 리스트에 모두 넣는다.
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 번호가 가장 작은 방을 먼저 방문해야 하므로 오름차순 정렬한다.
    for room in range(1, N + 1):
        graph[room].sort()

    # visited[room]은 room을 이미 처음 방문했는지 기록한다.
    visited = [False] * (N + 1)

    # next_index[room]은 graph[room]에서 다음에 확인할 위치이다.
    # 되돌아왔다가 다시 같은 방을 볼 때 처음부터 다시 훑지 않기 위해 사용한다.
    next_index = [0] * (N + 1)

    # stack은 현재 이동 경로이다.
    # 처음에는 1번 방에서 시작한다.
    stack = [1]
    visited[1] = True
    visit_order = [1]

    while stack:
        # 현재 위치는 stack의 맨 위 방이다.
        current = stack[-1]

        # 현재 방의 인접 방 목록에서 이미 방문한 방은 건너뛴다.
        # graph[current]가 정렬되어 있으므로, 이렇게 넘기면
        # 아직 방문하지 않은 방 중 가장 작은 방을 찾게 된다.
        while (
            next_index[current] < len(graph[current])
            and visited[graph[current][next_index[current]]]
        ):
            next_index[current] += 1

        # 인접 방을 끝까지 확인했다면 더 갈 곳이 없는 상태이다.
        # 왔던 길로 되돌아가기 위해 stack에서 현재 방을 뺀다.
        if next_index[current] == len(graph[current]):
            stack.pop()
            continue

        # 아직 방문하지 않은 가장 작은 번호의 인접 방이다.
        next_room = graph[current][next_index[current]]

        # 이 인접 방은 지금 선택했으므로 다음에는 그다음 위치부터 확인한다.
        next_index[current] += 1

        # next_room을 처음 방문한다.
        visited[next_room] = True
        visit_order.append(next_room)

        # 실제로 next_room으로 이동한 것처럼 stack에 넣는다.
        stack.append(next_room)

        # 모든 방을 처음 방문했다면 더 탐색할 필요가 없다.
        if len(visit_order) == N:
            break

    return visit_order


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    print(*solution(N, M, edges))
