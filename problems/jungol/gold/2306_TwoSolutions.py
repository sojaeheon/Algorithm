# JUNGOL 2306 두 용액
# 난이도: gold
# 분류: two_pointer, sorting
# 핵심:
#   두 용액의 합이 0에 가장 가까운 쌍을 찾는다.
#   정렬 후 가장 작은 값과 가장 큰 값에서 시작해 포인터를 움직인다.
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 용액의 수
#   values: 각 용액의 특성값
# - 출력:
#   합이 0에 가장 가까운 두 용액의 특성값
# - 조건:
#   두 용액은 서로 달라야 한다.
#   출력은 오름차순으로 한다.


# 2. 아이디어
# - 값을 정렬한다.
# - left는 가장 작은 값, right는 가장 큰 값에서 시작한다.
# - 현재 합이 0보다 작으면 합을 키워야 하므로 left를 오른쪽으로 옮긴다.
# - 현재 합이 0보다 크면 합을 줄여야 하므로 right를 왼쪽으로 옮긴다.
# - 매번 합의 절댓값이 더 작으면 정답 후보를 갱신한다.


# 3. 풀이 계획
# 1) values를 오름차순 정렬한다.
# 2) left = 0, right = N - 1로 둔다.
# 3) left < right인 동안 두 값을 더한다.
# 4) abs(합)이 가장 작으면 정답을 갱신한다.
# 5) 합의 부호에 따라 포인터를 이동한다.


def solution(N, values):
    values.sort()

    left = 0
    right = N - 1
    best_abs_sum = 10**18
    answer = [values[left], values[right]]

    while left < right:
        current_sum = values[left] + values[right]

        if abs(current_sum) < best_abs_sum:
            best_abs_sum = abs(current_sum)
            answer = [values[left], values[right]]

            if best_abs_sum == 0:
                break

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    values = list(map(int, input().split()))

    print(*solution(N, values))
