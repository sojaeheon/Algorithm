# JUNGOL 2497 수열
# 난이도: silver4
# 분류: prefix_sum, sliding_window
# 핵심:
#   길이가 K인 연속 구간의 합 중 최댓값을 구한다.
#   처음 K개 합을 만든 뒤, 왼쪽 값을 빼고 오른쪽 값을 더하며 구간을 한 칸씩 이동한다.
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 수열의 길이
#   K: 연속해서 더할 원소의 개수
#   numbers: 정수 수열
# - 출력:
#   길이가 K인 연속 부분 수열의 합 중 최댓값
# - 구해야 하는 것:
#   연속한 K개의 수를 골랐을 때 만들 수 있는 가장 큰 합


# 2. 아이디어
# - 모든 시작점마다 K개를 다시 더하면 O(NK)가 되어 비효율적이다.
# - 바로 이전 구간 합을 이용한다.
# - 예를 들어 [0 ~ K-1] 합을 알고 있다면,
#   다음 구간 [1 ~ K] 합은 이전 합에서 numbers[0]을 빼고 numbers[K]를 더하면 된다.
# - 이렇게 구간을 한 칸씩 밀면서 최댓값을 갱신한다.


# 3. 풀이 계획
# 1) 처음 K개 원소의 합을 구한다.
# 2) 그 값을 answer로 둔다.
# 3) K번째 인덱스부터 끝까지 확인한다.
# 4) 현재 합에서 빠지는 왼쪽 값을 빼고, 새로 들어오는 오른쪽 값을 더한다.
# 5) 매번 answer를 최댓값으로 갱신한다.


def solution(N, K, numbers):
    current_sum = sum(numbers[:K])
    answer = current_sum

    for right in range(K, N):
        left = right - K
        current_sum -= numbers[left]
        current_sum += numbers[right]

        if current_sum > answer:
            answer = current_sum

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(solution(N, K, numbers))
