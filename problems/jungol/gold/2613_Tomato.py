# JUNGOL 2613 토마토(고)
# 난이도: gold
# 분류: bfs, queue, graph
# 핵심:
#   처음부터 익어 있는 모든 토마토를 동시에 BFS 시작점으로 넣는다.
#   BFS의 거리/날짜가 토마토가 익는 최소 날짜가 된다.
# 시간 복잡도: O(NM)
# 공간 복잡도: O(NM)

from collections import deque
import sys


# 1. 문제 이해
# - 입력:
#   M: 상자의 가로 칸 수
#   N: 상자의 세로 칸 수
#   box: 토마토 상태
# - 출력:
#   모든 토마토가 익는 데 걸리는 최소 일수
#   끝까지 익지 못하는 토마토가 있으면 -1
# - 상태:
#   1: 익은 토마토
#   0: 익지 않은 토마토
#   -1: 토마토가 없는 칸


# 2. 아이디어
# - 익은 토마토가 여러 곳에서 동시에 퍼진다.
# - 이런 문제는 "시작점이 여러 개인 BFS"로 푼다.
# - 큐에 처음부터 익은 토마토 위치를 모두 넣고 시작한다.
# - 새로 익은 칸에는 이전 날짜 + 1을 기록한다.
# - 익지 않은 토마토 개수를 미리 세면, BFS 후 다시 전체를 훑지 않아도 된다.


# 3. 풀이 계획
# 1) 모든 칸을 확인하면서 1인 칸을 큐에 넣는다.
# 2) 0인 칸의 개수를 unripe_count에 저장한다.
# 3) BFS를 돌며 상하좌우의 0인 칸을 익힌다.
# 4) 토마토가 새로 익을 때마다 unripe_count를 1 줄인다.
# 5) BFS가 끝난 뒤 unripe_count가 남아 있으면 -1을 반환한다.
# 6) 아니면 마지막으로 익은 날짜를 반환한다.


def solution(N, M, box):
    queue = deque()
    unripe_count = 0

    for row in range(N):
        for col in range(M):
            if box[row][col] == 1:
                queue.append((row, col))
            elif box[row][col] == 0:
                unripe_count += 1

    if unripe_count == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    days = 0

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if next_row < 0 or next_row >= N:
                continue

            if next_col < 0 or next_col >= M:
                continue

            if box[next_row][next_col] != 0:
                continue

            box[next_row][next_col] = box[row][col] + 1
            days = box[next_row][next_col] - 1
            unripe_count -= 1
            queue.append((next_row, next_col))

    if unripe_count > 0:
        return -1

    return days


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, box))
