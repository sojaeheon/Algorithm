# JUNGOL 2000 동전교환
# 난이도: silver
# 분류: dp, unbounded_knapsack
# 핵심:
#   각 금액을 만드는 데 필요한 최소 동전 수를 저장한다.
#   같은 동전을 무제한 사용할 수 있다.
# 시간 복잡도: O(NW)
# 공간 복잡도: O(W)

import sys


# 1. 문제 이해
# - 입력:
#   N: 동전 종류 수 (1 <= N <= 10)
#   coins: 각 동전의 단위
#   W: 만들어야 하는 잔돈 (1 <= W <= 64,000)
# - 출력: 최소 동전 수, 만들 수 없으면 "impossible"


# 2. 아이디어
# - dp[money]를 money원을 만드는 최소 동전 수로 정의한다.
# - 만들 수 없는 상태는 충분히 큰 값 INF로 초기화한다.
# - 모든 동전은 무제한 사용할 수 있으므로 현재 금액에서 같은 동전을 다시 쓸 수 있다.


def solution(N, coins, W):
    INF = 10**9

    # dp[money] = money원을 만들 때 필요한 최소 동전 개수
    dp = [INF] * (W + 1)
    dp[0] = 0

    for money in range(1, W + 1):
        for coin in coins:
            if money < coin:
                continue

            dp[money] = min(dp[money], dp[money - coin] + 1)

    if dp[W] == INF:
        return "impossible"

    return dp[W]


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    coins = list(map(int, input().split()))
    W = int(input())

    print(solution(N, coins, W))
