# JUNGOL 2468 비밀번호
# 티어: gold
# 분류: math, bitmask, greedy
# 핵심:
#   이진수에서 1의 개수가 같은 수 중에서
#   A보다 작은 가장 가까운 수와 A보다 큰 가장 가까운 수를 찾는다.
# 시간 복잡도: O(log A)
#   A의 이진수 길이는 log A에 비례한다.
#   이진수 문자열을 오른쪽부터 한 번 훑고, 오른쪽 부분도 한 번 정리한다.
# 공간 복잡도: O(log A)
#   A의 이진수 문자열을 리스트로 저장하므로 이진수 길이만큼 공간을 사용한다.


# 1. 문제 이해
# - 입력:
#   A: 하나의 양의 정수, 1 <= A <= 10^18
# - 출력:
#   A보다 작으면서 이진수의 1의 개수가 같은 가장 가까운 수
#   A보다 크면서 이진수의 1의 개수가 같은 가장 가까운 수
#   두 수를 한 줄에 공백으로 구분해 출력
#   존재하지 않는 수는 0 출력
# - 구해야 하는 것:
#   같은 개수의 1 비트를 가지는 이전 수와 다음 수
# - 조건:
#   시간: 1초
#   메모리: 64MB


# 2. 아이디어
# - 큰 수 찾기:
#   오른쪽부터 01 패턴을 찾아 10으로 바꾼다.
#   바꾼 위치 오른쪽의 1들은 최대한 오른쪽으로 몰아 가장 작게 만든다.
# - 작은 수 찾기:
#   오른쪽부터 10 패턴을 찾아 01로 바꾼다.
#   바꾼 위치 오른쪽의 1들은 최대한 왼쪽으로 몰아 가장 크게 만든다.
# - 큰 수는 7 = 111 같은 경우도 처리해야 하므로 앞에 0을 붙여서 탐색한다.


# 3. 구현 계획
# 1) A를 이진수 문자열 리스트로 바꾼다.
# 2) 큰 수는 01, 작은 수는 10 패턴을 오른쪽부터 찾는다.
# 3) 패턴을 바꾼 뒤 오른쪽 비트를 정렬해 가장 가까운 수를 만든다.
# 4) 이진수 문자열을 다시 정수로 바꿔 반환한다.


def solution(A):
    def find_bigger():
        bits = list("0" + bin(A)[2:])

        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == "0" and bits[i + 1] == "1":
                bits[i], bits[i + 1] = "1", "0"

                right = bits[i + 2:]
                one_count = right.count("1")
                zero_count = len(right) - one_count
                bits[i + 2:] = ["0"] * zero_count + ["1"] * one_count

                return int("".join(bits), 2)

        return 0

    def find_smaller():
        bits = list(bin(A)[2:])

        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == "1" and bits[i + 1] == "0":
                bits[i], bits[i + 1] = "0", "1"

                right = bits[i + 2:]
                one_count = right.count("1")
                zero_count = len(right) - one_count
                bits[i + 2:] = ["1"] * one_count + ["0"] * zero_count

                return int("".join(bits), 2)

        return 0

    smaller = find_smaller()
    bigger = find_bigger()

    return smaller, bigger


if __name__ == "__main__":
    A = int(input())
    smaller, bigger = solution(A)

    print(smaller, bigger)
