# JUNGOL 8465 리어카 경주
# 난이도: gold
# 분류: graph, disjoint_set, union_find
# 핵심:
#   연결 관계를 분리 집합으로 관리하며 같은 그룹인지 빠르게 판단한다.
# 시간 복잡도: 입력 연산 수를 Q라 할 때 O(Q α(N))
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 이 문제는 연결되는 대상들을 그룹으로 합치고 연결 여부 또는 그룹 정보를 구한다.
# - 정확한 필드 단위 입력 해석은 문제 원문의 연산 형식에 맞춰 작성한다.


# 2. 아이디어
# - parent[x]는 x가 속한 집합의 대표를 가리킨다.
# - find에서는 경로 압축을 적용한다.
# - union에서는 크기 또는 rank가 작은 트리를 큰 트리 아래에 붙인다.


def solution(data):
    # TODO:
    # 1) 원문의 입력 형식대로 data를 파싱한다.
    # 2) parent와 size/rank 배열을 만든다.
    # 3) union/find 연산으로 정답을 계산한다.
    pass


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    answer = solution(data)

    if isinstance(answer, (list, tuple)):
        print(*answer, sep="\n")
    else:
        print(answer)
