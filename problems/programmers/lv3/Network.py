# Programmers 네트워크
# 난이도: LV3
# 분류: graph, dfs, bfs, connected_component
# 핵심:
#   컴퓨터들을 정점으로 보고, 연결 정보를 그래프로 해석한다.
#   아직 방문하지 않은 컴퓨터에서 탐색을 시작할 때마다 네트워크 수가 1개 늘어난다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N)


# 1. 문제 이해
# - 입력:
#   n: 컴퓨터의 개수
#   computers: 연결 여부를 나타내는 n x n 인접 행렬
# - 출력:
#   서로 연결된 컴퓨터 묶음, 즉 네트워크의 개수
# - 조건:
#   computers[i][j] == 1이면 i번 컴퓨터와 j번 컴퓨터가 연결되어 있다.
#   자기 자신은 항상 연결되어 있다.


# 2. 아이디어
# - 네트워크 하나는 그래프에서 하나의 연결 요소와 같다.
# - 방문하지 않은 컴퓨터를 발견하면 새로운 네트워크를 찾은 것이다.
# - 그 컴퓨터에서 DFS/BFS를 하며 연결된 컴퓨터를 모두 방문 처리한다.
# - 모든 컴퓨터를 확인하면 네트워크 개수를 알 수 있다.


# 3. 풀이 계획
# 1) visited 배열을 만든다.
# 2) 0번 컴퓨터부터 n - 1번 컴퓨터까지 확인한다.
# 3) 아직 방문하지 않은 컴퓨터를 만나면 answer를 1 증가시킨다.
# 4) 해당 컴퓨터에서 DFS 또는 BFS를 실행해 연결된 컴퓨터를 모두 방문 처리한다.
# 5) 모든 컴퓨터 확인 후 answer를 반환한다.

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue

        answer += 1
        queue = deque([start])
        visited[start] = True

        while queue:
            current_node = queue.popleft()

            for next_node in range(n):
                if computers[current_node][next_node] == 0:
                    continue

                if visited[next_node]:
                    continue

                visited[next_node] = True
                queue.append(next_node)

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0],
                       [1, 1, 0],
                       [0, 0, 1]]))  # 예상: 2

    print(solution(3, [[1, 1, 0],
                       [1, 1, 1],
                       [0, 1, 1]]))  # 예상: 1
