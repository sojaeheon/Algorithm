# JUNGOL 3706 합이 0이 되는 연속구간 세기
# 난이도: silver1
# 분류: prefix_sum, hash, dictionary
# 핵심:
#   누적합이 같은 두 지점 사이의 구간 합은 0이다.
#   지금까지 나온 누적합의 개수를 저장하면서 답을 더한다.
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

from collections import Counter
import sys


# 1. 문제 이해
# - 입력:
#   N: 수열의 길이
#   numbers: 정수 수열
# - 출력:
#   합이 0이 되는 연속 부분 구간의 개수
# - 조건:
#   정답이 커질 수 있으므로 Python int를 그대로 사용한다.


# 2. 아이디어
# - prefix[i]는 0번부터 i번 전까지의 누적합이다.
# - prefix[j] - prefix[i] == 0이면 i부터 j-1까지의 구간 합이 0이다.
# - 따라서 같은 누적합이 이전에 몇 번 나왔는지 세면 된다.
# - 시작 전에 누적합 0이 한 번 나온 것으로 처리한다.


# 3. 풀이 계획
# 1) prefix_count[0] = 1로 시작한다.
# 2) 숫자를 하나씩 더해 현재 누적합을 만든다.
# 3) 현재 누적합이 이전에 나온 횟수만큼 answer에 더한다.
# 4) 현재 누적합의 개수를 1 증가시킨다.


def solution(N, numbers):
    answer = 0
    prefix_count = Counter()
    prefix_count[0] = 1

    prefix_sum = 0

    for number in numbers:
        prefix_sum += number

        # 같은 누적합이 이전에 k번 있었다면,
        # 현재 위치에서 끝나는 합 0 구간이 k개 생긴다.
        answer += prefix_count[prefix_sum]
        prefix_count[prefix_sum] += 1

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    numbers = list(map(int, input().split()))

    print(solution(N, numbers))
