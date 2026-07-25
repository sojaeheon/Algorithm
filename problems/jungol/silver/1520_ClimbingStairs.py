# JUNGOL 1520 계단 오르기
# 난이도: silver
# 분류: dp
# 핵심:
#   마지막 계단은 반드시 밟고, 연속 세 계단을 밟지 않도록 이전 상태를 나눈다.
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 한 번에 1칸 또는 2칸을 오른다.
# - 연속된 계단 3개를 모두 밟을 수 없다.
# - 마지막 계단은 반드시 밟아야 한다.
# - 입력: 계단 수 N과 아래부터 차례대로 주어지는 각 계단 점수
# - 출력: 얻을 수 있는 최대 점수


# 2. 아이디어
# - dp[i]를 i번째 계단을 반드시 밟았을 때의 최대 점수로 정의한다.
# - i번째 계단에 오는 경우:
#   1) i-2번째 계단에서 두 칸 이동
#   2) i-3번째에서 i-1번째를 거쳐 한 칸 이동
# - N이 작은 경우를 위해 초기값을 따로 처리한다.


def solution(N, scores):
    # 계단 번호를 1부터 쓰기 위해 앞에 0을 붙인다.
    scores = [0] + scores

    if N == 1:
        return scores[1]

    if N == 2:
        return scores[1] + scores[2]

    dp = [0] * (N + 1)

    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]

    for stair in range(3, N + 1):
        # stair번째 계단을 밟는 방법은 두 가지이다.
        # 1) stair-2에서 두 칸 올라와 stair를 밟는다.
        # 2) stair-3에서 stair-1을 밟고, stair를 밟는다.
        #    이 경우 stair-2는 밟지 않으므로 연속 세 계단이 되지 않는다.
        dp[stair] = max(
            dp[stair - 2] + scores[stair],
            dp[stair - 3] + scores[stair - 1] + scores[stair],
        )

    return dp[N]


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    scores = [int(input()) for _ in range(N)]

    print(solution(N, scores))
