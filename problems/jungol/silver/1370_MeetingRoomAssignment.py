# JUNGOL 1370 회의실 배정
# 난이도: silver
# 분류: greedy, sorting
# 핵심:
#   끝나는 시간이 빠른 회의부터 선택하면 더 많은 회의를 배정할 수 있다.
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 회의의 수
#   meetings: (시작 시간, 끝나는 시간) 목록
# - 출력:
#   한 회의실에서 진행할 수 있는 회의의 최대 개수
# - 조건:
#   한 회의가 끝난 뒤 바로 다음 회의를 시작할 수 있는지 문제 조건을 확인한다.


# 2. 아이디어
# - 회의를 끝나는 시간 기준으로 정렬한다.
# - 끝나는 시간이 같으면 시작 시간이 빠른 순서로 정렬한다.
# - 현재 회의의 시작 시간이 마지막으로 선택한 회의의 종료 시간 이상이면 선택한다.


# 3. 풀이 계획
# 1) 회의 목록을 입력받는다.
# 2) (끝나는 시간, 시작 시간) 기준으로 정렬한다.
# 3) 가능한 회의를 앞에서부터 greedy하게 선택한다.


def solution(N, meetings):
    # TODO: greedy로 선택 가능한 회의 수를 구한다.
    answer = 0

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(N, meetings))
