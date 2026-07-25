# JUNGOL 1871 줄세우기
# 난이도: gold
# 분류: dp, lis
# 핵심:
#   이미 번호순으로 서 있는 가장 긴 증가 부분 수열은 옮기지 않아도 된다.
#   전체 아이 수에서 LIS 길이를 빼면 옮겨야 하는 최소 인원이 된다.
# 시간 복잡도: O(N^2), 이분 탐색 LIS를 사용하면 O(N log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력: 아이 수 N (2 <= N <= 200), 현재 줄의 번호 순서
# - 한 아이를 다른 위치로 옮길 수 있다.
# - 출력: 1번부터 N번까지 순서대로 만들기 위해 옮길 최소 인원


# 2. 아이디어
# - 현재 순서에서 이미 오름차순인 아이들은 위치를 유지할 수 있다.
# - 유지할 수 있는 최대 인원은 LIS의 길이이다.
# - 따라서 정답은 N - LIS 길이이다.


def solution(N, children):
    # TODO: children의 LIS 길이를 구해 N에서 뺀다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    children = [int(input()) for _ in range(N)]

    print(solution(N, children))
