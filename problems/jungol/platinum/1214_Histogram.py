# JUNGOL 1214 히스토그램
# 티어: platinum
# 분류: stack, monotone_stack
# 핵심:
#   스택에 높이가 오름차순이 되도록 막대의 인덱스를 저장한다.
#   현재 막대가 스택 top보다 낮아지는 순간,
#   top 막대는 더 이상 오른쪽으로 확장할 수 없으므로 넓이를 계산한다.
# 시간 복잡도: O(N)
#   각 막대 인덱스는 스택에 한 번 들어가고 한 번만 나오므로 전체 push/pop 횟수는 O(N)이다.
# 공간 복잡도: O(N)
#   높이가 계속 증가하는 경우 스택에 최대 N개의 인덱스가 저장될 수 있다.


# 1. 문제 이해
# - 입력:
#   n: 히스토그램을 이루는 직사각형의 개수, 1 <= n <= 100000
#   heights: 왼쪽부터 오른쪽 순서로 주어지는 n개의 높이
# - 출력:
#   히스토그램 안에서 만들 수 있는 가장 큰 직사각형의 넓이
# - 구해야 하는 것:
#   연속한 막대들로 만들 수 있는 직사각형 중 최대 넓이
# - 조건:
#   0 <= heights[i] <= 1000000000
#   각 직사각형의 너비는 1


# 2. 아이디어
# - 어떤 막대를 높이로 삼으면, 그 막대보다 낮은 막대가 나오기 전까지 좌우로 확장할 수 있다.
# - 스택에는 아직 오른쪽 경계가 확정되지 않은 막대의 인덱스를 저장한다.
# - 현재 높이가 스택 top의 높이보다 낮으면, top 막대의 오른쪽 경계가 현재 위치 바로 전으로 확정된다.
# - 끝에 높이 0을 추가하면 스택에 남은 막대들을 마지막에 모두 계산할 수 있다.


# 3. 구현 계획
# 1) heights 끝에 0을 추가한다.
# 2) 왼쪽부터 오른쪽까지 막대를 확인한다.
# 3) 현재 높이가 스택 top보다 낮으면 pop하며 넓이를 계산한다.
# 4) 현재 인덱스를 스택에 넣는다.
# 5) 계산한 넓이 중 최댓값을 반환한다.


def solution(n, heights):
    heights.append(0)
    stack = []
    result = 0

    for i in range(n + 1):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            result = max(result, height * width)

        stack.append(i)

    return result


if __name__ == "__main__":
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))

    n = data[0]
    heights = data[1:1 + n]

    answer = solution(n, heights)

    print(answer)
