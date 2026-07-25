# JUNGOL 1077 배낭채우기1
# 난이도: silver
# 분류: dp, unbounded_knapsack
# 핵심:
#   각 보석을 무제한 사용할 수 있는 완전 배낭 문제이다.
#   무게별로 얻을 수 있는 최대 값어치를 저장한다.
# 시간 복잡도: O(NW)
# 공간 복잡도: O(W)

import sys


# 1. 문제 이해
# - 입력:
#   N: 보석 종류 수 (1 <= N <= 1,000)
#   W: 배낭 용량 (1 <= W <= 10,000)
#   jewels: (무게, 값어치)
# - 각 보석은 무제한 사용할 수 있다.
# - 출력: 총 무게가 W 이하일 때 얻을 수 있는 최대 값어치


# 2. 아이디어
# - dp[capacity]를 capacity 이하에서 얻을 수 있는 최대 값어치로 정의한다.
# - 같은 보석을 여러 번 사용할 수 있도록 용량을 작은 쪽에서 큰 쪽으로 순회한다.
# - 0/1 배낭의 역순 순회와 차이를 구분한다.


def solution(N, W, jewels):
    dp = [0] * (W + 1)

    for weight, value in jewels:
        # 정방향으로 순회하면 같은 보석을 여러 번 사용할 수 있다.
        for current_weight in range(weight, W + 1):
            dp[current_weight] = max(
                dp[current_weight],
                dp[current_weight - weight] + value,
            )

    return dp[W]


if __name__ == "__main__":
    input = sys.stdin.readline

    N, W = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(N, W, jewels))
