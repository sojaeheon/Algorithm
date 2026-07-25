# JUNGOL 1220 최장 공통 부분서열
# 난이도: gold
# 분류: dp, string, lcs
# 핵심:
#   두 문자열의 앞부분에서 만들 수 있는 최장 공통 부분서열의 길이를 저장한다.
# 시간 복잡도: O(NM)
# 공간 복잡도: O(NM), 길이만 구하면 O(min(N, M))으로 줄일 수 있다.

import sys


# 1. 문제 이해
# - 두 문자열의 문자를 삭제하여 공통으로 만들 수 있는 가장 긴 부분서열을 찾는다.
# - 문자의 상대적인 순서는 바꿀 수 없다.
# - 입력은 EOF까지 두 줄이 한 테스트 케이스로 주어진다.
# - 각 테스트 케이스마다 LCS 길이를 출력한다.


# 2. 아이디어
# - dp[i][j]를 first[:i]와 second[:j]의 LCS 길이로 정의한다.
# - 두 문자가 같으면 dp[i-1][j-1] + 1이다.
# - 다르면 한쪽 문자를 제외한 두 상태 중 큰 값을 선택한다.


def solution(first, second):
    # TODO: LCS 점화식으로 최장 공통 부분서열의 길이를 계산한다.
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    answers = []

    for index in range(0, len(lines), 2):
        first = lines[index]
        second = lines[index + 1]
        answers.append(str(solution(first, second)))

    print("\n".join(answers))
