# JUNGOL 5205 장난감조립
# 난이도: gold
# 분류: graph, topological_sort, dp
# 핵심:
#   부품 조립 관계를 DAG로 보고 필요한 기본 부품 개수를 전파한다.
# 시간 복잡도: O(NM) 수준
# 공간 복잡도: O(N^2 + M)

import sys


# 1. 문제 이해
# - 완제품 N을 만들기 위한 기본 부품별 필요 개수를 구한다.
# - 관계 (X, Y, K)는 X를 만들 때 Y가 K개 필요하다는 뜻이다.
# - 중간 부품은 출력하지 않고 기본 부품만 번호순으로 출력한다.


# 2. 아이디어
# - 기본 부품에서 중간/완제품 방향으로 조립 관계를 연결한다.
# - need[part][basic]에 part 하나를 만드는 데 필요한 기본 부품 수를 저장한다.
# - 진입 차수가 0인 기본 부품부터 위상정렬하며 개수를 전파한다.


def solution(N, relations):
    # TODO: 위상정렬 DP로 완제품 N에 필요한 기본 부품 개수를 구한다.
    # return [(기본 부품 번호, 필요 개수), ...]
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    relations = [tuple(map(int, input().split())) for _ in range(M)]

    for part, count in solution(N, relations):
        print(part, count)
