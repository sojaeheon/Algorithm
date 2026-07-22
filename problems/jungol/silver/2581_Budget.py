# JUNGOL 2581 예산
# 난이도: silver
# 분류: binary_search, parametric_search
# 핵심:
#   상한액을 정하면 배정되는 총 예산을 계산할 수 있다.
#   총 예산이 제한 이하가 되는 가장 큰 상한액을 이분 탐색으로 찾는다.
# 시간 복잡도: O(N log M)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 지방의 수
#   requests: 각 지방의 예산 요청액
#   total_budget: 전체 예산
# - 출력:
#   가능한 예산 상한액의 최댓값
# - 조건:
#   요청액이 상한액보다 크면 상한액만 배정한다.
#   요청액이 상한액 이하이면 요청액 그대로 배정한다.


# 2. 아이디어
# - 상한액 cap을 정하면 총 배정액은 sum(min(request, cap))으로 계산된다.
# - 총 배정액이 total_budget 이하이면 cap을 더 키워볼 수 있다.
# - 총 배정액이 total_budget을 넘으면 cap을 줄여야 한다.


# 3. 풀이 계획
# 1) left = 0, right = max(requests)로 둔다.
# 2) mid를 상한액으로 정하고 총 배정액을 계산한다.
# 3) 가능하면 answer를 갱신하고 left를 키운다.
# 4) 불가능하면 right를 줄인다.


def solution(N, requests, total_budget):
    left = 0
    right = max(requests)
    answer = 0

    while left <= right:
        cap = (left + right) // 2

        used_budget = 0
        for request in requests:
            used_budget += min(request, cap)

        if used_budget <= total_budget:
            answer = cap
            left = cap + 1
        else:
            right = cap - 1

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    requests = list(map(int, input().split()))
    total_budget = int(input())

    print(solution(N, requests, total_budget))
