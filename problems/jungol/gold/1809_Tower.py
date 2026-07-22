# JUNGOL 1809 탑
# 난이도: gold
# 분류: stack, monotone_stack
# 핵심:
#   왼쪽에 있는 탑 중 현재 탑의 신호를 받을 수 있는 가장 가까운 탑을 찾는다.
#   현재 탑보다 낮은 탑은 이후에도 신호를 받을 수 없으므로 stack에서 제거한다.
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 탑의 개수
#   heights: 왼쪽부터 오른쪽까지 탑의 높이
# - 출력:
#   각 탑의 신호를 수신하는 탑의 번호
# - 조건:
#   탑 번호는 1번부터 시작한다.
#   왼쪽 방향으로 신호를 보낸다고 생각한다.


# 2. 아이디어
# - stack에는 "아직 오른쪽 탑의 신호를 받을 가능성이 있는 탑"만 남긴다.
# - 현재 탑보다 낮은 탑은 현재 탑에게 가려지므로 pop한다.
# - pop 이후 stack top이 있으면 그 탑이 현재 탑의 신호를 받는다.
# - stack이 비면 받을 탑이 없으므로 0이다.


# 3. 풀이 계획
# 1) 왼쪽부터 탑을 하나씩 확인한다.
# 2) stack top의 높이가 현재 탑보다 낮으면 제거한다.
# 3) stack top이 남아 있으면 그 번호를 answer에 넣는다.
# 4) 현재 탑을 stack에 넣는다.


def solution(N, heights):
    answer = []
    stack = []

    for tower_number, height in enumerate(heights, start=1):
        # 현재 탑보다 낮은 탑은 현재 탑의 신호를 받을 수 없다.
        while stack and stack[-1][1] < height:
            stack.pop()

        if stack:
            answer.append(stack[-1][0])
        else:
            answer.append(0)

        stack.append((tower_number, height))

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    heights = list(map(int, input().split()))

    print(*solution(N, heights))
