# JUNGOL 2993 리조트
# 난이도: gold
# 분류: dp, memoization
# 핵심:
#   날짜와 보유 쿠폰 수를 상태로 두고 1일권, 3일권, 5일권 구매를 비교한다.
#   리조트에 가지 않는 날은 비용 없이 다음 날로 이동한다.
# 시간 복잡도: O(N × 가능한 쿠폰 수)
# 공간 복잡도: O(N × 가능한 쿠폰 수)

import sys


# 1. 문제 이해
# - N일까지 리조트를 이용해야 하며, 가지 않는 M개의 날짜가 주어진다.
# - 이용권:
#   1일권 10,000원
#   3일권 25,000원 + 쿠폰 1장
#   5일권 37,000원 + 쿠폰 2장
# - 쿠폰 3장으로 하루를 무료 이용할 수 있다.
# - 출력: 필요한 최소 비용


# 2. 아이디어
# - dp(day, coupons)를 day일부터 마지막 날까지 필요한 최소 비용으로 정의한다.
# - 가지 않는 날이면 비용 없이 day + 1로 이동한다.
# - 가는 날이면 1일권, 3일권, 5일권과 쿠폰 사용 가능성을 비교한다.
# - 여러 날 이용권은 날짜를 넘겨 이동하고 쿠폰을 추가한다.


def solution(N, M, closed_days):
    # TODO: 날짜와 쿠폰 수를 상태로 최소 비용을 계산한다.
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    closed_days = set(map(int, input().split())) if M else set()

    print(solution(N, M, closed_days))
