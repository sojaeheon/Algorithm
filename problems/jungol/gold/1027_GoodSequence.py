# JUNGOL 1027 좋은수열
# 분류: 백트래킹, DFS
# 핵심: 1, 2, 3을 작은 순서로 붙이고, 새로 생긴 마지막 부분만 검사한다.

import sys


def is_good(sequence):
    """마지막 숫자를 붙인 뒤 같은 두 부분 수열이 인접했는지 검사한다."""
    length = len(sequence)

    # 비교할 두 부분 수열의 길이
    for size in range(1, length // 2 + 1):
        if sequence[length - 2 * size : length - size] == sequence[length - size :]:
            return False

    return True


def solution(n):
    sequence = []

    def dfs():
        if len(sequence) == n:
            return True

        # 작은 숫자부터 시도하므로 처음 완성된 수열이 정답이다.
        for number in "123":
            sequence.append(number)

            if is_good(sequence) and dfs():
                return True

            sequence.pop()

        return False

    dfs()
    return "".join(sequence)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    print(solution(N))
