# JUNGOL 2587 달리기
# 난이도: platinum
# 분류: coordinate_compression, fenwick_tree
# 핵심:
#   현재 선수의 최고 등수는
#   "앞에 있는 선수 중 현재 선수보다 실력이 좋은 선수 수 + 1"이다.
#   실력 값을 좌표 압축한 뒤 Fenwick Tree로 앞선 선수들의 실력 개수를 관리한다.
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 선수의 수
#   abilities: 선수들의 실력 목록
# - 출력:
#   각 선수가 현재 순서에서 얻을 수 있는 최고 등수
# - 구해야 하는 것:
#   i번째 선수보다 앞에 있는 선수 중, i번째 선수보다 실력이 좋은 선수의 수


# 2. 아이디어
# - 단순히 앞에 있는 모든 선수를 확인하면 O(N^2)이므로 느리다.
# - 실력 값의 범위가 클 수 있으므로 좌표 압축을 한다.
# - 압축 번호는 작은 실력부터 1, 2, 3...으로 붙인다.
# - 이미 등장한 선수들의 실력 개수를 Fenwick Tree에 저장한다.
# - 현재 선수의 압축 실력이 rank라면,
#   현재 선수보다 실력이 좋은 선수는 rank + 1 ~ max_rank 구간에 있다.
# - 따라서 better_count = query(max_rank) - query(rank)이다.
# - 현재 선수의 최고 등수는 better_count + 1이다.


# 3. 풀이 계획
# 1) 실력 배열을 좌표 압축한다.
# 2) Fenwick Tree를 준비한다.
# 3) 선수들을 입력 순서대로 확인한다.
# 4) 현재 선수보다 실력이 좋은 앞선 선수 수를 구한다.
# 5) better_count + 1을 answer에 저장한다.
# 6) 현재 선수의 실력을 Fenwick Tree에 추가한다.


def solution(N, abilities):
    sorted_values = sorted(set(abilities))
    compressed = {
        value: index
        for index, value in enumerate(sorted_values, start=1)
    }

    size = len(sorted_values)
    tree = [0] * (size + 1)

    def update(index, value):
        while index <= size:
            tree[index] += value
            index += index & -index

    def query(index):
        total = 0

        while index > 0:
            total += tree[index]
            index -= index & -index

        return total

    answer = []

    for ability in abilities:
        rank = compressed[ability]

        total_runner_count = query(size)
        not_better_count = query(rank)
        better_count = total_runner_count - not_better_count

        answer.append(better_count + 1)
        update(rank, 1)

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    abilities = []
    for _ in range(N):
        abilities.append(int(input()))

    answer = solution(N, abilities)

    print("\n".join(map(str, answer)))
