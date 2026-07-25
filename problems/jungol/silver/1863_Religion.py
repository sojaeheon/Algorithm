# JUNGOL 1863 종교
# 난이도: silver
# 분류: graph, disjoint_set, union_find
# 핵심:
#   같은 종교라고 알려진 학생들을 하나의 집합으로 합친다.
#   마지막에 남은 서로 다른 대표의 수가 가능한 종교의 최대 가짓수다.
# 시간 복잡도: O((N + M) α(N))
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 학생 수 N은 최대 50,000, 같은 종교인 학생 쌍 M은 최대 100,000이다.
# - 입력된 각 쌍은 반드시 같은 집합에 속한다.
# - 출력: 주어진 정보와 모순되지 않는 최대 종교 가짓수


# 2. 아이디어
# - 처음에는 각 학생이 서로 다른 종교라고 가정한다.
# - 같은 종교인 쌍마다 두 집합을 union한다.
# - union에 성공할 때마다 집합 수를 1 줄이면 마지막 값이 정답이다.


def solution(N, pairs):
    # TODO: 경로 압축과 union by size/rank를 사용해 집합 수를 계산한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    pairs = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, pairs))
