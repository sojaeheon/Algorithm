# JUNGOL 1912 미로 탐색
# 난이도: silver
# 분류: graph, dfs, stack, sorting
# 핵심:
#   1번 방에서 시작해 아직 방문하지 않은 인접 방 중 번호가 가장 작은 방으로 이동한다.
#   더 갈 수 있는 방이 없으면 왔던 길로 되돌아간다.
#   실제로 처음 방문한 방의 순서를 출력한다.
# 시간 복잡도: O((N + M) log M)
# 공간 복잡도: O(N + M)

import sys


# 1. 문제 이해
# - 입력:
#   N: 방의 수
#   M: 문의 수
#   M개의 줄: 서로 연결된 두 방 a, b
# - 출력:
#   동현이가 처음 방문한 순서대로 N개의 방 번호 출력
# - 조건:
#   모든 방은 연결되어 있다.
#   현재 방에서 방문하지 않은 방이 여러 개면 번호가 가장 작은 방으로 간다.


# 2. 아이디어
# - 그래프의 인접 리스트를 만든다.
# - 각 방의 인접 방 목록을 오름차순 정렬한다.
# - DFS처럼 이동하되, 각 방마다 다음에 확인할 인접 방 위치를 기억한다.
# - 재귀 DFS는 N이 100,000까지 가능하므로 깊이가 커질 수 있다.
# - 따라서 stack으로 직접 구현하는 방식이 안전하다.


# 3. 풀이 계획
# 1) graph[a].append(b), graph[b].append(a)로 양방향 그래프를 만든다.
# 2) 각 graph[node]를 오름차순 정렬한다.
# 3) 1번 방을 방문 처리하고 stack에 넣는다.
# 4) stack top 방에서 아직 방문하지 않은 가장 작은 인접 방을 찾는다.
# 5) 찾으면 방문 순서에 추가하고 stack에 넣는다.
# 6) 더 갈 곳이 없으면 stack에서 pop해서 되돌아간다.


def solution(N, M, edges):
    # TODO: 문제 풀이 로직 작성
    # return visit_order
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    answer = solution(N, M, edges)

    # TODO: answer가 리스트라면 아래처럼 출력한다.
    # print(*answer)
