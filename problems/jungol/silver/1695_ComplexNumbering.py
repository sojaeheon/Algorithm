# JUNGOL 1695 단지번호붙이기
# 문제: https://jungol.co.kr/problem/1695
# 난이도: Silver 1
# 분류: graph, dfs, bfs, connected_component
# 핵심:
#   지도에서 집이 있는 칸을 상하좌우로 탐색하여 각 단지의 크기를 구한다.
#   단지별 집의 수를 오름차순으로 정렬해 출력한다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N^2)

import sys


# 1. 문제 이해
# - N x N 지도에서 1은 집, 0은 빈 공간이다.
# - 상하좌우로 연결된 집들을 하나의 단지로 센다.
# - 단지 수와 각 단지에 속한 집의 수를 오름차순으로 출력한다.


# 2. 아이디어
# - 모든 칸을 순회하면서 아직 방문하지 않은 집을 찾는다.
# - 해당 집에서 DFS 또는 BFS를 시작해 연결된 집의 수를 센다.
# - 각 단지의 크기를 저장한 뒤 오름차순으로 정렬한다.

from collections import deque

def solution(N, grid):
    # 정답
    answer = []
    check = [[False] * N for _ in range(N)]

    # 상,하,좌,우 확인
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            # 집이 없거나 이미 다른 단지에서 방문한 칸은 건너뛴다.
            if grid[r][c] == 0 or check[r][c]:
                continue

            queue = deque([(r, c)])
            check[r][c] = True
            house_count = 0

            while queue:
                current_r, current_c = queue.popleft()
                house_count += 1

                for direction in range(4):
                    next_r = current_r + dr[direction]
                    next_c = current_c + dc[direction]

                    if not (0 <= next_r < N and 0 <= next_c < N):
                        continue
                    if grid[next_r][next_c] == 0 or check[next_r][next_c]:
                        continue

                    check[next_r][next_c] = True
                    queue.append((next_r, next_c))

            answer.append(house_count)

    answer.sort()
    return answer
if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    complex_sizes = solution(N, grid)

    print(len(complex_sizes))
    print(*complex_sizes, sep="\n")
