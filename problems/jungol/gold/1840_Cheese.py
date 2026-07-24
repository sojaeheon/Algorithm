# JUNGOL 1840 치즈
# 난이도: gold3
# 분류: bfs, queue, simulation
# 핵심:
#   바깥 공기와 닿은 치즈만 한 시간마다 녹는다.
#   매 시간 (0, 0)에서 BFS로 바깥 공기를 찾고, 닿은 치즈를 녹인다.
# 시간 복잡도: O(TNM), T는 치즈가 모두 녹는 데 걸리는 시간
# 공간 복잡도: O(NM)

from collections import deque
import sys


# 1. 문제 이해
# - 입력:
#   N: 세로 크기
#   M: 가로 크기
#   board: 치즈 지도
# - 출력:
#   치즈가 모두 녹는 데 걸리는 시간
#   모두 녹기 한 시간 전에 남아 있던 치즈 칸 수
# - 상태:
#   0: 공기
#   1: 치즈


# 2. 아이디어
# - 치즈 안쪽의 구멍은 바깥 공기가 아니므로 바로 녹지 않는다.
# - 따라서 매 시간 바깥 공기만 BFS로 탐색해야 한다.
# - 바깥 공기와 맞닿은 치즈를 모아두었다가 한꺼번에 녹인다.


# 3. 풀이 계획
# 1) 현재 남은 치즈 개수를 센다.
# 2) 남은 치즈가 0이 될 때까지 반복한다.
# 3) BFS로 바깥 공기를 탐색한다.
# 4) 바깥 공기와 닿은 치즈 좌표를 melt 리스트에 모은다.
# 5) melt에 있는 치즈를 모두 0으로 바꾼다.
# 6) 시간과 마지막 치즈 개수를 갱신한다.


def solution(N, M, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 현재 남아 있는 치즈 칸 수를 먼저 센다.
    cheese_count = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                cheese_count += 1

    time = 0
    last_cheese_count = cheese_count

    # 치즈가 남아 있는 동안 한 시간씩 시뮬레이션한다.
    while cheese_count > 0:
        # 이번 시간이 시작되기 직전에 남아 있던 치즈 개수이다.
        # 마지막 반복에서 이 값이 "모두 녹기 한 시간 전 치즈 개수"가 된다.
        last_cheese_count = cheese_count

        visited = [[False] * M for _ in range(N)]
        queue = deque()
        melt = []

        # 판의 가장자리에는 치즈가 없다고 했으므로 (0, 0)은 항상 바깥 공기이다.
        queue.append((0, 0))
        visited[0][0] = True

        # 바깥 공기만 BFS로 탐색한다.
        # 치즈 내부의 구멍은 바깥 공기와 연결되어 있지 않으므로 여기서 방문되지 않는다.
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if next_row < 0 or next_row >= N:
                    continue

                if next_col < 0 or next_col >= M:
                    continue

                if visited[next_row][next_col]:
                    continue

                visited[next_row][next_col] = True

                if board[next_row][next_col] == 1:
                    # 바깥 공기와 닿은 치즈이다.
                    # 같은 시간 안에 바로 0으로 바꾸면 탐색이 그 안쪽으로 들어갈 수 있으므로,
                    # melt에 모아두었다가 BFS가 끝난 뒤 한꺼번에 녹인다.
                    melt.append((next_row, next_col))
                else:
                    # 빈 칸이면 바깥 공기가 계속 이어지는 칸이므로 큐에 넣는다.
                    queue.append((next_row, next_col))

        for row, col in melt:
            board[row][col] = 0

        cheese_count -= len(melt)
        time += 1

    return time, last_cheese_count


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    time, last_count = solution(N, M, board)
    print(time)
    print(last_count)
