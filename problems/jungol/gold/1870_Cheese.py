# JUNGOL 1870 치즈
# 문제: https://jungol.co.kr/problem/1870
# 난이도: Gold 2
# 분류: graph, bfs, simulation
# 핵심:
#   외부 공기와 두 변 이상 접촉한 치즈를 한 시간마다 녹인다.
#   치즈 내부의 빈 공간은 외부 공기와 구분해야 한다.
# 시간 복잡도: O(T x N x M)
# 공간 복잡도: O(N x M)

import sys
from collections import deque


# 1. 문제 이해
# - N x M 모눈종이에서 1은 치즈, 0은 빈 공간이다.
# - 외부 공기와 두 변 이상 맞닿은 치즈는 한 시간 후 녹는다.
# - 치즈로 둘러싸인 내부 공간은 외부 공기가 아니다.
# - 모든 치즈가 녹는 데 걸리는 시간을 출력한다.


# 2. 아이디어
# - 매 시간 가장자리의 빈 공간에서 BFS를 시작해 외부 공기를 찾는다.
# - 각 치즈 칸의 상하좌우 중 외부 공기인 칸의 수를 센다.
# - 외부 공기와 두 변 이상 접촉한 치즈를 동시에 녹인다.
# - 치즈가 모두 없어질 때까지 반복한다.


def solution(N, M, board):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    elapsed_time = 0

    while True:
        # (0, 0)에서 도달할 수 있는 빈칸만 현재의 외부 공기이다.
        outside_air = [[False] * M for _ in range(N)]
        outside_air[0][0] = True
        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()

            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col

                if not (0 <= next_row < N and 0 <= next_col < M):
                    continue
                if outside_air[next_row][next_col]:
                    continue
                if board[next_row][next_col] == 1:
                    continue

                outside_air[next_row][next_col] = True
                queue.append((next_row, next_col))

        melting = []

        for row in range(N):
            for col in range(M):
                if board[row][col] == 0:
                    continue

                exposed_sides = 0

                for delta_row, delta_col in directions:
                    next_row = row + delta_row
                    next_col = col + delta_col

                    if outside_air[next_row][next_col]:
                        exposed_sides += 1

                if exposed_sides >= 2:
                    melting.append((row, col))

        if not melting:
            return elapsed_time

        # 같은 시간에 녹는 치즈가 서로에게 영향을 주지 않도록 한꺼번에 제거한다.
        for row, col in melting:
            board[row][col] = 0

        elapsed_time += 1


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, board))
