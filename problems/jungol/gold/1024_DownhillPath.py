# JUNGOL 1024 내리막 길
# 난이도: gold
# 분류: dp, dfs, memoization, graph
# 핵심:
#   현재 칸보다 낮은 칸으로만 이동하며 도착점까지 가는 경로 수를 센다.
#   같은 칸에서 도착점까지 가는 경로 수를 메모이제이션한다.
# 시간 복잡도: O(NM)
# 공간 복잡도: O(NM)

import sys


# 1. 문제 이해
# - 입력: 지도 크기 N, M과 각 칸의 높이
# - 이동: 상하좌우 중 현재 칸보다 높이가 낮은 칸
# - 출력: 왼쪽 위에서 오른쪽 아래까지 가는 내리막 경로의 수


# 2. 아이디어
# - dfs(row, col)를 현재 칸에서 도착점까지 가는 경로 수로 정의한다.
# - 도착점에서는 경로 하나를 완성했으므로 1을 반환한다.
# - 아직 계산하지 않은 칸만 DFS하고 결과를 memo에 저장한다.
# - 낮은 칸으로만 가므로 높이가 계속 감소하여 사이클이 없다.


def solution(N, M, heights):
    # TODO: DFS + 메모이제이션으로 경로 수를 계산한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    sys.setrecursionlimit(1_000_000)

    N, M = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, heights))
