# JUNGOL 1696 미로만들기
# 문제: https://jungol.co.kr/problem/1696

import sys
from collections import deque


def solution(N, board):
    INF = float("inf")
    min_changes = [[INF] * N for _ in range(N)]
    min_changes[0][0] = 0

    queue = deque([(0, 0)])
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        row, col = queue.popleft()

        for delta_row, delta_col in directions:
            next_row = row + delta_row
            next_col = col + delta_col

            if not (0 <= next_row < N and 0 <= next_col < N):
                continue

            change_cost = 0 if board[next_row][next_col] == 1 else 1
            next_changes = min_changes[row][col] + change_cost

            if next_changes >= min_changes[next_row][next_col]:
                continue

            min_changes[next_row][next_col] = next_changes

            if change_cost == 0:
                queue.appendleft((next_row, next_col))
            else:
                queue.append((next_row, next_col))

    return min_changes[N - 1][N - 1]


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    print(solution(N, board))
