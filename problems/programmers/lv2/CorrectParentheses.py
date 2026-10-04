# Programmers 올바른 괄호
# 난이도: LV2
# 분류: stack, string
# 핵심:
#   여는 괄호 '('는 쌓고, 닫는 괄호 ')'가 나올 때마다
#   앞에 짝이 되는 여는 괄호가 있는지 확인한다.
# 시간 복잡도:
# 공간 복잡도:


# 1. 문제 이해
# - 입력:
#   s: '('와 ')'로만 이루어진 문자열
# - 출력:
#   올바른 괄호 문자열이면 True, 아니면 False
# - 올바른 괄호:
#   여는 괄호와 닫는 괄호의 짝이 순서에 맞게 맞는 문자열


# 2. 아이디어
# - '('가 나오면 stack에 넣는다.
# - ')'가 나오면 stack에서 '(' 하나를 제거한다.
# - 그런데 ')'가 나왔는데 stack이 비어 있으면 짝이 없으므로 False이다.
# - 모든 문자를 본 뒤 stack이 비어 있어야 True이다.


# 3. 풀이 계획
# 1) 빈 stack을 만든다.
# 2) 문자열 s를 왼쪽부터 확인한다.
# 3) '('이면 stack에 넣는다.
# 4) ')'이면 stack이 비었는지 확인하고, 비어 있지 않으면 하나 뺀다.
# 5) 마지막에 stack이 비어 있으면 True, 남아 있으면 False를 반환한다.


def solution(s):
    answer = True

    # TODO: stack을 이용해 올바른 괄호인지 확인한다.

    return answer


if __name__ == "__main__":
    print(solution("()()"))  # 예상: True
    print(solution("(())()"))  # 예상: True
    print(solution(")()("))  # 예상: False
    print(solution("(()("))  # 예상: False
