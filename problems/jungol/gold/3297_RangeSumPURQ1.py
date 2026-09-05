# JUNGOL 3297 구간의 합(PURQ) 1
# 난이도: Gold 1
# 분류: data_structure, fenwick_tree, prefix_sum, purq
# 핵심:
#   점 갱신은 기존 값과 새 값의 차이를 반영하고, 구간 합은 두 누적합의 차로 구한다.
# 시간 복잡도: 명령당 O(log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 초깃값이 주어진 길이 N의 수열에 점 갱신(Point Update)과 구간 합(Range Query)을 수행한다.
# - 명령 1 k value: k번째 값을 value로 입력하거나 수정한다.
# - 명령 2 start end: [start, end] 구간의 합을 출력한다.


# 2. 아이디어
# - Fenwick Tree에 각 위치까지의 누적합 정보를 저장한다.
# - 값 변경 시 delta = new_value - old_value를 트리에 더한다.
# - 구간 합은 prefix_sum(end) - prefix_sum(start - 1)이다.


def solution(N, values, commands):
    # step 1. 펜윅 트리 갱신 함수
    def update(i, diff):
        while i <= N:
            tree[i] += diff
            i += i & -i

    # step 2. 1~i까지 합 구하는 함수
    def prefix_sum(i):
        result = 0
        while i > 0:
            result += tree[i]
            i -= i & -i

        return result

    # step 3. 특정 구간 합 구하기
    def range_sum(left, right):
        return prefix_sum(right) - prefix_sum(left - 1)

    # step 4. 초기 배열로 펜윅 트리 만들기: O(N)
    tree = [0] + values[:]
    for i in range(1, N + 1):
        parent = i + (i & -i)
        if parent <= N:
            tree[parent] += tree[i]

    # step 5. 명령 처리하기
    answers = []

    for command, first, second in commands:
        if command == 1:
            index, new_value = first, second
            diff = new_value - values[index - 1]
            values[index - 1] = new_value
            update(index, diff)
        else:
            left, right = first, second
            answers.append(range_sum(left, right))

    return answers

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    values = list(map(int, input().split()))
    M = int(input())
    commands = [tuple(map(int, input().split())) for _ in range(M)]

    print(*solution(N, values, commands), sep="\n")
