# JUNGOL 2300 용액
# 난이도: gold
# 분류: two_pointer, sorting
# 핵심:
#   두 용액의 합이 0에 가장 가까운 쌍을 찾는다.
#   정렬 후 양끝 포인터를 움직이면 O(N)에 탐색할 수 있다.
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
#   출력 순서가 오름차순인지 문제 조건을 확인한다.


# 2. 아이디어
# - 값을 정렬한다.
# - left는 가장 작은 값, right는 가장 큰 값에서 시작한다.
# - 두 값의 합이 0보다 작으면 합을 키우기 위해 left를 오른쪽으로 옮긴다.
# - 두 값의 합이 0보다 크면 합을 줄이기 위해 right를 왼쪽으로 옮긴다.
# - 절댓값이 가장 작은 합을 만드는 쌍을 저장한다.


# 3. 풀이 계획
# 1) values를 정렬한다.
# 2) left, right 투 포인터를 둔다.
# 3) 현재 합의 절댓값이 더 작으면 정답 후보를 갱신한다.
# 4) 합의 부호에 따라 포인터를 이동한다.


def solution(N, values):
    values.sort()

    left = 0
    right = N - 1
    best_sum = 10**18
    answer = [values[left], values[right]]

    while left < right:
        current_sum = values[left] + values[right]

        if abs(current_sum) < best_sum:
            best_sum = abs(current_sum)
            answer = [values[left], values[right]]

            if best_sum == 0:
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
