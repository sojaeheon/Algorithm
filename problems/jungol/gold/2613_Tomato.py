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


# 3. 풀이 계획
# 1) 모든 칸을 확인하면서 1인 칸을 큐에 넣는다.
# 2) BFS를 돌며 상하좌우의 0인 칸을 익힌다.
# 3) BFS가 끝난 뒤 0이 남아 있으면 -1을 반환한다.
# 4) 아니면 가장 큰 날짜 - 1을 반환한다.


def solution(N, M, box):
    # TODO: 문제 풀이 로직 작성
    # return days
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, box))
