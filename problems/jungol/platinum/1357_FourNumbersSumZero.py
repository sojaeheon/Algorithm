# JUNGOL 1357 합이 0이 되는 4개의 숫자들
# 난이도: platinum
# 분류: meet_in_the_middle, hash, counter
# 핵심:
#   A + B + C + D = 0을 (A + B) = -(C + D)로 나누어 생각한다.
#   A+B로 만들 수 있는 합의 개수를 Counter에 저장한다.
#   C+D를 만들면서 그 반대값이 A+B에 몇 번 있었는지 더한다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N^2)

from collections import Counter
import sys


# 1. 문제 이해
# - 입력:
#   N: 각 배열의 원소 개수
#   A, B, C, D: 각각 N개의 정수를 가진 배열
# - 출력:
#   A[i] + B[j] + C[k] + D[l] == 0 이 되는 경우의 수
# - 구해야 하는 것:
#   네 배열에서 각각 하나씩 선택했을 때 합이 0이 되는 조합의 개수


# 2. 아이디어
# - 4중 반복은 O(N^4)이므로 불가능하다.
# - 네 배열을 A+B와 C+D 두 묶음으로 나눈다.
# - A+B의 합이 x라면, C+D의 합은 -x여야 전체 합이 0이 된다.
# - A+B로 만들 수 있는 모든 합을 Counter에 개수로 저장한다.
# - C+D를 만들면서 필요한 값인 -(C+D)가 몇 개 있었는지 더한다.


# 3. 풀이 계획
# 1) 입력을 A, B, C, D 네 배열로 나누어 저장한다.
# 2) A+B로 만들 수 있는 모든 합을 Counter에 저장한다.
# 3) C+D를 하나씩 만들면서 target = -(C+D)를 구한다.
# 4) sum_ab[target]을 answer에 더한다.
# 5) answer를 출력한다.


# 4. Counter와 defaultdict 차이
# - Counter는 없는 key를 조회해도 0을 반환하고 key를 새로 만들지 않는다.
# - defaultdict(int)는 없는 key를 []로 조회하면 0을 반환하면서 key를 새로 만든다.
# - 이 문제에서 defaultdict를 쓰고 answer += sum_ab[target]을 하면,
#   A+B에 없는 target까지 C+D 탐색 중에 계속 추가되어 메모리 초과가 날 수 있다.
# - defaultdict를 꼭 쓴다면 answer += sum_ab.get(target, 0)처럼 get()을 써야 key가 추가되지 않는다.


# 5. bisect 대안
# - C+D 합 리스트를 정렬하고 A+B의 반대값을 bisect로 찾는 방법도 있다.
# - 하지만 N=4000이면 A+B가 16,000,000개라 bisect_left/right 호출이 너무 많아질 수 있다.
# - 이 문제에서는 해시 조회가 평균 O(1)이므로 Counter 풀이가 시간 면에서 유리하다.


def solution(N, A, B, C, D):
    sum_ab = Counter()

    for a in A:
        for b in B:
            sum_ab[a + b] += 1

    answer = 0

    for c in C:
        for d in D:
            answer += sum_ab[-(c + d)]

    return answer


def main():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    N = int(data[0])

    A = []
    B = []
    C = []
    D = []

    index = 1
    for _ in range(N):
        A.append(int(data[index]))
        B.append(int(data[index + 1]))
        C.append(int(data[index + 2]))
        D.append(int(data[index + 3]))
        index += 4

    print(solution(N, A, B, C, D))


if __name__ == "__main__":
    main()
