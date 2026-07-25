# JUNGOL 1411 두 줄로 타일 깔기
# 난이도: silver
# 분류: dp
# 핵심:
#   2×N 판의 마지막을 채우는 방법을 기준으로 점화식을 세운다.
#   정답이 커지므로 매 단계에서 20100529로 나눈다.
# 시간 복잡도: O(N)
# 공간 복잡도: O(N), 이전 값만 저장하면 O(1)

import sys


# 1. 문제 이해
# - 입력: 세로 칸 수 N (1 <= N <= 100,000)
# - 출력: 2×N 판을 채우는 방법의 수를 20100529로 나눈 나머지


# 2. 아이디어
# - dp[i]를 2×i 판을 채우는 방법의 수로 정의한다.
# - 마지막 한 열 또는 마지막 두 열을 어떤 타일로 채웠는지 구분한다.
# - 작은 N의 값을 직접 그려 초기값과 점화식을 확인한다.
# - dp[1] = 1, dp[2] = 3
# - dp[n] = dp[n - 1] + 2 * dp[n - 2]


def solution(N):
    MOD = 20100529

    if N == 1:
        return 1

    # previous_two = dp[i - 2]
    # previous_one = dp[i - 1]
    previous_two = 1
    previous_one = 3

    for _ in range(3, N + 1):
        current = (previous_one + 2 * previous_two) % MOD
        previous_two = previous_one
        previous_one = current

    return previous_one


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    print(solution(N))
