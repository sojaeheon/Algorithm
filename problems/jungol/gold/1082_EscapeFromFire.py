# JUNGOL 1082 화염에서탈출
# 난이도: gold2
# 분류: bfs, queue, simulation
# 핵심:
#   불이 먼저 언제 도착하는지 BFS로 계산한다.
#   그 다음 사람이 이동할 때 불보다 먼저 도착할 수 있는 칸만 이동한다.
# 시간 복잡도: O(RC)
# 공간 복잡도: O(RC)

from collections import deque
import sys


# 1. 문제 이해
# - 입력:
#   R: 행의 수
#   C: 열의 수
#   grid: 지도
# - 출력:
#   시작 위치에서 집/목적지까지 도착하는 최소 시간
#   도착할 수 없으면 문제에서 요구하는 실패 문구 출력
# - 지도 문자:
#   S: 시작 위치
#   D: 목적지
#   *: 불
#   X: 바위
#   .: 빈 칸


# 2. 아이디어
# - 불과 사람이 동시에 움직이는 문제이다.
# - 안전하게 처리하려면 불의 도착 시간을 먼저 구한다.
# - 사람이 어떤 칸에 t초에 도착하려고 할 때,
#   불이 그 칸에 t초 이하로 도착한다면 이동할 수 없다.
# - 목적지 D는 불이 번지지 않는 칸으로 처리한다.


# 3. 풀이 계획
# 1) 지도에서 시작 위치, 목적지, 불 위치들을 찾는다.
# 2) 모든 불 위치를 큐에 넣고 BFS를 돌려 fire_time을 만든다.
# 3) 시작 위치에서 사람 BFS를 돌린다.
# 4) 다음 칸이 벽이 아니고, 불보다 먼저 도착 가능하면 이동한다.
# 5) 목적지에 도착하면 시간을 반환한다.
# 6) 끝까지 도착하지 못하면 실패 값을 반환한다.


def solution(R, C, grid):
    INF = 10**9
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    fire_queue = deque()
    start = None
    destination = None

    # 지도에서 시작점, 목적지, 불의 위치를 찾는다.
    # 불은 여러 개일 수 있으므로 모두 큐에 넣는다.
    for row in range(R):
        for col in range(C):
            if grid[row][col] == "S":
                start = (row, col)
            elif grid[row][col] == "D":
                destination = (row, col)
            elif grid[row][col] == "*":
                fire_queue.append((row, col))

    # fire_time[row][col]은 불이 해당 칸에 처음 도착하는 시간이다.
    # INF는 불이 도착하지 못하는 칸이라는 뜻이다.
    fire_time = [[INF] * C for _ in range(R)]

    for row, col in fire_queue:
        fire_time[row][col] = 0

    # 1단계: 불 BFS
    # 불은 빈 칸과 시작 위치로 퍼질 수 있지만,
    # 바위 X와 집 D에는 퍼지지 못한다고 처리한다.
    while fire_queue:
        row, col = fire_queue.popleft()

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if next_row < 0 or next_row >= R:
                continue

            if next_col < 0 or next_col >= C:
                continue

            if grid[next_row][next_col] == "X":
                continue

            if grid[next_row][next_col] == "D":
                continue

            if fire_time[next_row][next_col] != INF:
                continue

            fire_time[next_row][next_col] = fire_time[row][col] + 1
            fire_queue.append((next_row, next_col))

    # 2단계: 사람 BFS
    # person_time[row][col]은 사람이 해당 칸에 도착하는 시간이다.
    person_time = [[-1] * C for _ in range(R)]
    person_queue = deque()

    start_row, start_col = start
    person_time[start_row][start_col] = 0
    person_queue.append((start_row, start_col))

    while person_queue:
        row, col = person_queue.popleft()

        # 목적지에 도착하면 BFS 특성상 이 시간이 최소 시간이다.
        if (row, col) == destination:
            return person_time[row][col]

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if next_row < 0 or next_row >= R:
                continue

            if next_col < 0 or next_col >= C:
                continue

            if grid[next_row][next_col] == "X":
                continue

            if person_time[next_row][next_col] != -1:
                continue

            next_time = person_time[row][col] + 1

            # 불이 같은 시간 또는 더 먼저 도착하는 칸은 갈 수 없다.
            # 목적지 D는 fire_time이 INF로 남아 있으므로 이 조건을 통과한다.
            if fire_time[next_row][next_col] <= next_time:
                continue

            person_time[next_row][next_col] = next_time
            person_queue.append((next_row, next_col))

    return "impossible"


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    R, C = map(int, input().split())
    grid = [list(input().decode().strip()) for _ in range(R)]

    print(solution(R, C, grid))
