# JUNGOL 2606 토마토(초)
# 난이도: gold5
# 분류: bfs, queue, graph, simulation
# 핵심:
#   3차원 상자에서 처음부터 익어 있는 모든 토마토를 동시에 BFS 시작점으로 넣는다.
#   상하좌우앞뒤 6방향으로 익음이 퍼지며, BFS 거리가 최소 날짜가 된다.
# 시간 복잡도: O(HNM)
# 공간 복잡도: O(HNM)

from collections import deque
import sys


# 1. 문제 이해
# - 입력:
#   M: 상자의 가로 칸 수
#   N: 상자의 세로 칸 수
#   H: 상자의 높이
#   box: H개의 층마다 N행 M열의 토마토 상태
# - 출력:
#   모든 토마토가 익는 데 걸리는 최소 일수
#   끝까지 익지 못하는 토마토가 있으면 -1
# - 상태:
#   1: 익은 토마토
#   0: 익지 않은 토마토
#   -1: 토마토가 없는 칸


# 2. 아이디어
# - 익은 토마토가 여러 개일 수 있으므로 모든 익은 토마토를 큐에 넣고 시작한다.
# - 3차원이므로 한 칸에서 이동할 수 있는 방향은 6개이다.
#   같은 층 상하좌우 + 위층 + 아래층
# - 새로 익은 토마토에는 이전 칸의 날짜 + 1을 기록한다.
# - 익지 않은 토마토 수를 미리 세면 BFS가 끝난 뒤 전체 상자를 다시 확인하지 않아도 된다.


# 3. 풀이 계획
# 1) 모든 칸을 확인하면서 1인 칸을 큐에 넣는다.
# 2) 0인 칸의 개수를 unripe_count에 저장한다.
# 3) BFS를 돌며 6방향의 0인 칸을 익힌다.
# 4) 토마토가 새로 익을 때마다 unripe_count를 1 줄인다.
# 5) BFS가 끝난 뒤 unripe_count가 남아 있으면 -1을 반환한다.
# 6) 아니면 마지막으로 익은 날짜를 반환한다.


def solution(M, N, H, box):
    queue = deque()
    unripe_count = 0

    for height in range(H):
        for row in range(N):
            for col in range(M):
                if box[height][row][col] == 1:
                    queue.append((height, row, col))
                elif box[height][row][col] == 0:
                    unripe_count += 1

    if unripe_count == 0:
        return 0

    directions = [
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
        (-1, 0, 0),
        (1, 0, 0),
    ]

    days = 0

    while queue:
        height, row, col = queue.popleft()

        for dh, dr, dc in directions:
            next_height = height + dh
            next_row = row + dr
            next_col = col + dc

            if next_height < 0 or next_height >= H:
                continue

            if next_row < 0 or next_row >= N:
                continue

            if next_col < 0 or next_col >= M:
                continue

            if box[next_height][next_row][next_col] != 0:
                continue

            box[next_height][next_row][next_col] = box[height][row][col] + 1
            days = box[next_height][next_row][next_col] - 1
            unripe_count -= 1
            queue.append((next_height, next_row, next_col))

    if unripe_count > 0:
        return -1

    return days


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    M, N, H = map(int, input().split())

    box = []
    for _ in range(H):
        layer = [list(map(int, input().split())) for _ in range(N)]
        box.append(layer)

    print(solution(M, N, H, box))
