# JUNGOL 1997 떡 먹는 호랑이
# 티어: silver
# 분류: dp, brute_force, fibonacci
# 핵심:
#   첫째 날 떡 개수를 A, 둘째 날 떡 개수를 B라고 하면
#   D일째 떡 개수는 x*A + y*B 형태로 표현할 수 있다.
#   x, y는 피보나치처럼 앞의 두 계수를 더해 구한다.
# 시간 복잡도: O(D + K)
#   D일째 계수를 구할 때 D번 정도 계산하고,
#   가능한 A를 1부터 K까지 최악의 경우 모두 확인할 수 있다.
# 공간 복잡도: O(D)
#   각 날짜별 A 계수와 B 계수를 배열에 저장하므로 D에 비례한다.


# 1. 문제 이해
# - 입력:
#   D: 할머니가 호랑이를 만난 날, 3 <= D <= 30
#   K: D일째 호랑이에게 준 떡의 개수, 10 <= K <= 100000
# - 출력:
#   첫째 날 준 떡의 개수 A
#   둘째 날 준 떡의 개수 B
# - 구해야 하는 것:
#   D일째 떡 개수가 K가 되도록 하는 자연수 A, B


# 2. 아이디어
# - 1일째: A = 1*A + 0*B
# - 2일째: B = 0*A + 1*B
# - 3일째부터는 전날 + 전전날이다.
# - 따라서 A의 계수와 B의 계수도 피보나치처럼 변한다.
# - D일째 계수를 x, y라고 하면 x*A + y*B = K이다.
# - A를 1부터 넣어 보면서 자연수 B가 나오는 값을 찾는다.


# 3. 구현 계획
# 1) D일째의 A 계수 x, B 계수 y를 구한다.
# 2) A를 1부터 하나씩 대입한다.
# 3) K - x*A가 y로 나누어떨어지면 B를 구한다.
# 4) A, B를 반환한다.


def solution(D, K):
    a_coef = [0] * (D + 1)
    b_coef = [0] * (D + 1)

    a_coef[1] = 1
    b_coef[1] = 0
    a_coef[2] = 0
    b_coef[2] = 1

    for day in range(3, D + 1):
        a_coef[day] = a_coef[day - 1] + a_coef[day - 2]
        b_coef[day] = b_coef[day - 1] + b_coef[day - 2]

    x = a_coef[D]
    y = b_coef[D]

    for A in range(1, K + 1):
        remain = K - x * A

        if remain <= 0:
            break

        if remain % y == 0:
            B = remain // y

            if A <= B:
                return A, B

    return None


if __name__ == "__main__":
    D, K = map(int, input().split())
    A, B = solution(D, K)

    print(A)
    print(B)
