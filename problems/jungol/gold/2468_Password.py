# JUNGOL 2468 비밀번호
# 티어: gold
# 분류: math, bitmask, greedy
# 핵심:
#
# 시간 복잡도:
# 공간 복잡도:


# 1. 문제 이해
# - 입력:
#   A: 하나의 양의 정수, 1 <= A <= 10^18
# - 출력:
#   A보다 작으면서 이진수의 1의 개수가 같은 가장 가까운 수
#   A보다 크면서 이진수의 1의 개수가 같은 가장 가까운 수
#   두 수를 한 줄에 공백으로 구분해 출력
#   존재하지 않는 수는 0 출력
# - 구해야 하는 것:
#   TODO: 문제에서 요구하는 값 정리
# - 조건:
#   시간: 1초
#   메모리: 64MB


# 2. 아이디어
# - TODO: 어떤 규칙이 있는가?
# - TODO: 어떤 값을 상태로 둘 것인가?
# - TODO: 수학 / 비트마스크 / 그리디 중 어떤 방식이 어울리는가?


# 3. 구현 계획
# 1)
# 2)
# 3)


def solution(A):
    # TODO: 문제 해결 로직 작성
    # return smaller, bigger
    
    # 큰값 찾는 함수
    def big_search(A):
        bits = list('0'+ bin(A)[2:])
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == '0' and bits[i+1] == '1':
                bits[i], bits[i+1] = '1','0'

                right = bits[i + 2:]
                one_count = right.count('1')
                zero_count = len(right) - one_count
                bits[i + 2:] = ['0'] * zero_count + ['1'] * one_count

                return int(''.join(bits), 2)

        return 0
    
    def small_search(A):
        bits = list(bin(A)[2:])
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == '1' and bits[i+1] == '0':
                bits[i], bits[i+1] = '0','1'

                right = bits[i + 2:]
                one_count = right.count('1')
                zero_count = len(right) - one_count
                bits[i + 2:] = ['1'] * one_count + ['0'] * zero_count

                return int(''.join(bits), 2)

        return 0
    
    
    # 숫자 x
    bigger = big_search(A)
    smaller = small_search(A)

    return smaller,bigger



if __name__ == "__main__":
    A = int(input())

    answer = solution(A)

    # TODO: 정답 출력 형식에 맞게 수정
    print(*answer)
