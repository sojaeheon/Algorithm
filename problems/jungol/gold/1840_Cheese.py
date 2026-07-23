# JUNGOL 1840 치즈
# 난이도: gold
# 분류: bfs, queue, simulation
# 핵심:
#   바깥 공기와 닿은 치즈만 한 시간마다 녹는다.
#   매 시간 (0, 0)에서 BFS로 바깥 공기를 찾고, 닿은 치즈를 녹인다.
# 시간 복잡도: O(TNM)
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
    # TODO: 문제 풀이 로직 작성
    # return time, last_cheese_count
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    time, last_count = solution(N, M, board)
    print(time)
    print(last_count)
