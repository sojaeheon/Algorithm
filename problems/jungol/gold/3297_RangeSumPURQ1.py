# JUNGOL 3297 구간의 합(PURQ) 1
# 난이도: gold
# 분류: data_structure, fenwick_tree, prefix_sum, purq
# 핵심:
#   점 갱신은 기존 값과 새 값의 차이를 반영하고, 구간 합은 두 누적합의 차로 구한다.
# 시간 복잡도: 명령당 O(log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 길이 N의 수열에 점 갱신(Point Update)과 구간 합(Range Query)을 수행한다.
# - 명령 1 k value: k번째 값을 value로 입력하거나 수정한다.
# - 명령 2 start end: [start, end] 구간의 합을 출력한다.


# 2. 아이디어
# - Fenwick Tree에 각 위치까지의 누적합 정보를 저장한다.
# - 값 변경 시 delta = new_value - old_value를 트리에 더한다.
# - 구간 합은 prefix_sum(end) - prefix_sum(start - 1)이다.


def solution(N, commands):
    # TODO: Fenwick Tree로 명령을 처리하고 질의 결과 목록을 반환한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    commands = [tuple(map(int, input().split())) for _ in range(M)]

    print(*solution(N, commands), sep="\n")
